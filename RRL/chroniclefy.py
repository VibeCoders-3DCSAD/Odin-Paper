#!/usr/bin/env python3
"""
Mega‑compiler with optional prefix filter, content‑based duplicate detection,
and optional keyword filtering.
Scans subfolders (except those starting with '0') for *_summarized.md files
that start with a given prefix (e.g., "I--" or "L--"), extracts sections,
and appends only new (content‑unique) files that contain a given keyword
(if specified) to chronicle.md in the root.

Usage:
    python mega_compiler.py                     # all files
    python mega_compiler.py --prefix "I--"      # only files starting with I--
    python mega_compiler.py -p "L--"            # only files starting with L--
    python mega_compiler.py -k "Random Forest"  # only files mentioning "Random Forest"
    python mega_compiler.py -p "I--" -k "LLM"   # combine filters
"""

import argparse
import hashlib
import re
from pathlib import Path
from typing import Dict, Optional, List, Set, Tuple

SECTIONS = [
    "TL;DR",
    "Findings",
    "Relevance to Odin",
    "Limitations",
]


def file_hash(file_path: Path) -> str:
    """Compute SHA‑256 hash of file contents."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def extract_title(content: str) -> str:
    """Extract first level‑1 heading."""
    match = re.search(r"^# (.*?)$", content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_section(content: str, section_name: str) -> Optional[str]:
    """Extract content under a ## heading until next # or ## or EOF."""
    escaped_name = re.escape(section_name)
    pattern = rf"(?m)^## {escaped_name}\s*\n(.*?)(?=^# |^## |\Z)"
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else None


def format_entry(rel_path: Path, title: str, sections: Dict[str, Optional[str]]) -> str:
    """Build a markdown block for a single summarized file."""
    lines = [
        f"## Source: `{rel_path.as_posix()}`",
        "",
        f"**Title:** {title}",
        "",
    ]
    for section in SECTIONS:
        content = sections.get(section)
        if content:
            lines.append(f"### {section}")
            lines.append("")
            lines.append(content)
            lines.append("")
    return "\n".join(lines).strip()


def get_processed_hashes(root_path: Path, chronicle_path: Path) -> Set[str]:
    """
    Read chronicle.md, extract all source file paths, compute hash of each file
    (if it still exists), and return a set of those hashes.
    """
    processed_hashes = set()
    if not chronicle_path.exists():
        return processed_hashes

    try:
        content = chronicle_path.read_text(encoding="utf-8")
    except Exception:
        return processed_hashes

    # Find all '## Source: `path`' lines
    pattern = r"^## Source: `(.*?)`$"
    source_paths = re.findall(pattern, content, re.MULTILINE)

    for rel_path_str in source_paths:
        candidate_file = root_path / rel_path_str
        if candidate_file.exists() and candidate_file.is_file():
            try:
                processed_hashes.add(file_hash(candidate_file))
            except Exception:
                pass
        else:
            print(f"  ⚠️ Warning: previously recorded file not found: {rel_path_str}")

    return processed_hashes


def contains_keyword(text: str, keyword: str) -> bool:
    """Case‑insensitive check if keyword appears anywhere in the text."""
    if not keyword or not text:
        return False
    return keyword.lower() in text.lower()


def process_folder(folder_path: Path, root_path: Path,
                   processed_hashes: Set[str], prefix: Optional[str],
                   keyword: Optional[str]) -> List[Tuple[Path, str]]:
    """
    Scan a folder for *_summarized.md files (optionally prefix‑filtered),
    extract sections, and return a list of (relative_path, formatted_entry)
    for files whose content hash is NOT already in processed_hashes
    AND (if keyword is given) the keyword appears in title or any section.
    """
    if prefix:
        pattern = f"{prefix}*_summarized.md"
    else:
        pattern = "*_summarized.md"

    files = list(folder_path.glob(pattern))
    if not files:
        return []

    files.sort()
    new_entries = []

    for file_path in files:
        rel_path = file_path.relative_to(root_path)

        # Compute hash of the entire file (for duplicate detection)
        try:
            hash_val = file_hash(file_path)
        except Exception as e:
            print(f"  ⚠️ Could not hash {file_path}: {e}")
            continue

        if hash_val in processed_hashes:
            print(f"  ⏭️ Skipping duplicate content: {rel_path.as_posix()} (already in chronicle.md)")
            continue

        # Extract sections and title
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ⚠️ Could not read {file_path}: {e}")
            continue

        title = extract_title(content)
        sections_data = {s: extract_section(content, s) for s in SECTIONS}

        if title == "Untitled" and all(v is None for v in sections_data.values()):
            print(f"  ⚠️ No relevant sections in {file_path}")
            continue

        # --- KEYWORD FILTERING ---
        if keyword:
            # Build a single string from title + all non‑None section contents
            searchable_text = title + " " + " ".join(
                text for text in sections_data.values() if text
            )
            if not contains_keyword(searchable_text, keyword):
                print(f"  ⏭️ Skipping (keyword '{keyword}' not found): {rel_path.as_posix()}")
                continue
            else:
                print(f"  ✅ Keyword '{keyword}' found in: {rel_path.as_posix()}")
        # --- END KEYWORD FILTERING ---

        # Mark as processed now to avoid adding the same file twice in the same run
        processed_hashes.add(hash_val)
        new_entries.append((rel_path, format_entry(rel_path, title, sections_data)))

    return new_entries


def main():
    parser = argparse.ArgumentParser(
        description="Mega‑compiler: aggregate only new (content‑unique) summaries into chronicle.md"
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root directory to scan for subfolders (default: current directory)",
    )
    parser.add_argument(
        "-p", "--prefix",
        type=str,
        default=None,
        help="Only include *_summarized.md files whose name starts with this prefix (e.g., 'I--' or 'L--')"
    )
    parser.add_argument(
        "-k", "--keyword",
        type=str,
        default=None,
        help="Only include summaries that contain this word/phrase (case‑insensitive) in the title or any section"
    )
    args = parser.parse_args()

    root_path = Path(args.root).resolve()
    if not root_path.is_dir():
        print(f"Error: '{root_path}' is not a valid directory.")
        return

    # Find immediate subdirectories, exclude those starting with '0'
    all_subdirs = [
        d for d in root_path.iterdir()
        if d.is_dir() and not d.name.startswith("0")
    ]

    if not all_subdirs:
        print(f"No eligible subdirectories found in {root_path} (ignoring folders starting with '0')")
        return

    chronicle_path = root_path / "chronicle.md"
    processed_hashes = get_processed_hashes(root_path, chronicle_path)

    if processed_hashes:
        print(f"Found {len(processed_hashes)} unique content hashes already in {chronicle_path.name}")
    else:
        print(f"{chronicle_path.name} does not exist or contains no previous entries.")

    prefix_info = f" with prefix '{args.prefix}'" if args.prefix else " (no prefix filter)"
    keyword_info = f" with keyword '{args.keyword}'" if args.keyword else " (no keyword filter)"
    print(f"Scanning {len(all_subdirs)} folders{prefix_info}{keyword_info}...")
    for d in sorted(all_subdirs):
        print(f"  - {d.name}")

    all_new_entries = []

    for folder in sorted(all_subdirs):
        print(f"\n📁 Scanning '{folder.name}':")
        new_entries = process_folder(folder, root_path, processed_hashes, args.prefix, args.keyword)
        if new_entries:
            print(f"  → Found {len(new_entries)} new file(s)")
            all_new_entries.extend(new_entries)
        else:
            print(f"  → No new files in {folder.name}")

    if not all_new_entries:
        print("\nNo new (content‑unique) summaries to add. chronicle.md unchanged.")
        return

    # Append only the formatted entries
    output_content = "\n\n---\n\n".join(entry for _, entry in all_new_entries) + "\n"

    if chronicle_path.exists():
        current = chronicle_path.read_text(encoding="utf-8")
        if current.rstrip().endswith("---"):
            final = current.rstrip() + "\n\n" + output_content
        else:
            final = current.rstrip() + "\n\n---\n\n" + output_content
        chronicle_path.write_text(final, encoding="utf-8")
        print(f"\n✓ Appended {len(all_new_entries)} new entries to existing {chronicle_path}")
    else:
        chronicle_path.write_text(output_content, encoding="utf-8")
        print(f"\n✓ Created {chronicle_path} with {len(all_new_entries)} entries")

    print(f"Total new (content‑unique) summaries added: {len(all_new_entries)}")
    print("\nAdded files:")
    for rel_path, _ in all_new_entries:
        print(f"  - {rel_path.as_posix()}")


if __name__ == "__main__":
    main()