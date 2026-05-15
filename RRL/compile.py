import sys
import re
import yaml
from pathlib import Path
from typing import Dict, Optional, Tuple


def extract_frontmatter(content: str) -> Tuple[Dict, str]:
    def parse_yaml(block: str) -> Dict:
        try:
            result = yaml.safe_load(block)
            return result if isinstance(result, dict) else {}
        except yaml.YAMLError as e:
            print(f"Warning: YAML parsing error: {e}", file=sys.stderr)
            return {}
        
    if content.startswith("---\n"):
        end_idx = content.find("\n---\n", 4)
        if end_idx != -1:
            return parse_yaml(content[4:end_idx]), content[end_idx + 5:]
        
    match = re.search(r"```yaml\s*\n---\s*\n(.*?)\n---\s*\n```", content, re.DOTALL)
    if match:
        return parse_yaml(match.group(1)), content

    return {}, content

def extract_tldr(body: str) -> Optional[str]:
    match = re.search(r"^## TL;DR\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL | re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def extract_relevance_subsections(body: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    relevance_match = re.search(
        r"^## Relevance to Odin\s*\n(.*?)(?=\n## |\Z)",
        body, re.DOTALL | re.MULTILINE
    )
    if not relevance_match:
        return None, None, None, None

    section = relevance_match.group(1)

    def extract_block(marker: str) -> Optional[str]:
        pattern = rf"\*\*{re.escape(marker)}:\*\*\s*\n(.*?)(?=\n\*\*|\Z)"
        match = re.search(pattern, section, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None

    topics = extract_block("Topics")
    contribution = extract_block("Contribution to Odin")
    directly = extract_block("Directly justifies")
    limits = extract_block("Limits of relevance")

    return topics, contribution, directly, limits

def process_one_file(file_path: Path) -> Optional[str]:
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

    frontmatter, body = extract_frontmatter(content)

    title = frontmatter.get("title", file_path.stem)
    authors = frontmatter.get("authors", "Unknown authors")
    if isinstance(authors, str):
        authors = authors.replace(";", ",")
    year = frontmatter.get("year", "")
    odin_topics = frontmatter.get("odin_topics", [])

    tldr = extract_tldr(body)
    if not tldr:
        print(f"Warning: No TL;DR found in {file_path}", file=sys.stderr)
        tldr = "*No TL;DR provided*"

    topics, contribution, directly, limits = extract_relevance_subsections(body)

    lines = []
    lines.append(f"# {title}")
    lines.append(f"*by {authors}{f', {year}' if year else ''}*")
    lines.append("")
    lines.append("## TL;DR")
    lines.append(tldr)
    lines.append("")

    if topics:
        lines.append("## Topics")
        lines.append(topics)
        lines.append("")

    if contribution:
        lines.append("## Contribution to Odin")
        lines.append(contribution)
        lines.append("")

    if directly:
        lines.append("**Directly justifies:**")
        lines.append(directly)
        lines.append("")

    if limits:
        lines.append("**Limits of relevance:**")
        lines.append(limits)
        lines.append("")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Compile multiple markdown review files into one."
    )
    parser.add_argument(
        "input_dir", nargs="?", default=".",
        help="Directory containing .md files (default: current directory)"
    )
    parser.add_argument(
        "-o", "--output", default="compiled_reviews.md",
        help="Output markdown file (default: compiled_reviews.md)"
    )
    parser.add_argument(
        "--glob", default="*.md",
        help="Glob pattern for markdown files (default: *.md)"
    )
    args = parser.parse_args()

    input_path = Path(args.input_dir)
    if not input_path.is_dir():
        print(f"Error: {input_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(input_path.glob(args.glob))
    if not md_files:
        print(f"No markdown files found matching {args.glob} in {input_path}")
        sys.exit(0)

    sections = []
    for md_file in md_files:
        print(f"Processing {md_file.name}...")
        section = process_one_file(md_file)
        if section:
            sections.append(section)

    if not sections:
        print("No valid sections extracted. Exiting.")
        sys.exit(0)

    output_content = "\n".join(sections)
    output_path = Path(args.output)
    output_path.write_text(output_content, encoding="utf-8")
    print(f"Compiled {len(sections)} sections into {output_path}")


if __name__ == "__main__":
    main()