#!/usr/bin/env python3
"""
Extract specific sections (TL;DR, Findings, Relevance to Odin, Limitations)
from *_summarized.md files and append them to <directory>_Compilation.md.

Usage:
    python compile_summaries.py /path/to/directory
"""

import argparse
import re
from pathlib import Path
from typing import Dict, Optional


# Only these sections will be extracted
SECTIONS = [
    "TL;DR",
    "Findings",
    "Relevance to Odin",
    "Limitations",
]


def extract_title(content: str) -> str:
    """Extract the first level-1 heading (e.g., '# Title')."""
    match = re.search(r"^# (.*?)$", content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def extract_section(content: str, section_name: str) -> Optional[str]:
    """
    Extract the content of a level-2 section (e.g., '## TL;DR').
    Returns text from the heading line until the next level-1 or level-2 heading,
    or end of file.
    """
    escaped_name = re.escape(section_name)
    pattern = rf"(?m)^## {escaped_name}\s*\n(.*?)(?=^# |^## |\Z)"
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def format_for_compilation(file_path: Path, title: str, sections: Dict[str, Optional[str]]) -> str:
    """Build the markdown block for one summarized file using only requested sections."""
    lines = []
    lines.append(f"## Source: `{file_path.name}`")
    lines.append("")
    lines.append(f"**Title:** {title}")
    lines.append("")
    for section in SECTIONS:
        content = sections.get(section)
        if content:
            lines.append(f"### {section}")
            lines.append("")
            lines.append(content)
            lines.append("")
    return "\n".join(lines).strip()


def process_file(file_path: Path) -> Optional[str]:
    """Read a file, extract title and requested sections, return formatted block."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return None

    title = extract_title(content)
    sections_data = {}
    for section in SECTIONS:
        sections_data[section] = extract_section(content, section)

    # Only add file if at least one requested section or title is meaningful
    if title == "Untitled" and all(v is None for v in sections_data.values()):
        print(f"Warning: No requested sections found in {file_path}")
        return None

    return format_for_compilation(file_path, title, sections_data)


def main():
    parser = argparse.ArgumentParser(
        description="Compile TL;DR, Findings, Relevance to Odin, and Limitations from *_summarized.md files"
    )
    parser.add_argument(
        "directory", type=str, help="Directory containing the summarized markdown files"
    )
    args = parser.parse_args()

    root_dir = Path(args.directory).resolve()
    if not root_dir.is_dir():
        print(f"Error: '{root_dir}' is not a valid directory.")
        return

    # Find all .md files ending with '_summarized.md'
    pattern = "*_summarized.md"
    files = list(root_dir.glob(pattern))
    if not files:
        print(f"No files matching '{pattern}' found in {root_dir}")
        return

    files.sort()  # deterministic order

    # Output file name: <directory_name>_Compilation.md
    dir_name = root_dir.name  # e.g., 'reports' from /home/user/reports
    compilation_path = root_dir / f"{dir_name}_Compilation.md"

    blocks = []

    for file_path in files:
        print(f"Processing: {file_path.name}")
        block = process_file(file_path)
        if block:
            blocks.append(block)

    if not blocks:
        print("No usable content extracted. Compilation file not updated.")
        return

    output_content = "\n\n---\n\n".join(blocks) + "\n"

    if compilation_path.exists():
        # Append with separator
        current = compilation_path.read_text(encoding="utf-8")
        if current.rstrip().endswith("---"):
            final = current.rstrip() + "\n\n" + output_content
        else:
            final = current.rstrip() + "\n\n---\n\n" + output_content
        compilation_path.write_text(final, encoding="utf-8")
        print(f"Appended to existing {compilation_path}")
    else:
        compilation_path.write_text(output_content, encoding="utf-8")
        print(f"Created {compilation_path}")

    print(f"Successfully compiled {len(blocks)} file(s).")


if __name__ == "__main__":
    main()