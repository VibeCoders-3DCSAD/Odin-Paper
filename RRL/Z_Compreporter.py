#!/usr/bin/env python3
"""
Megascript: Compile reports from summary .md files.
Filter by subtopic OR by filename prefix (prefix mode never skips files).
"""

import argparse
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

def find_summaries_folder() -> Path:
    cwd = Path.cwd()
    matches = [p for p in cwd.rglob("*") if p.is_dir() and "summaries" in p.name.lower()]
    if not matches:
        raise FileNotFoundError("No --folder provided and no folder containing 'Summaries' found.")
    matches.sort(key=lambda p: len(p.relative_to(cwd).parts))
    return matches[0]

def extract_fields_from_md(file_path: Path) -> Optional[Dict[str, Any]]:
    try:
        content = file_path.read_text(encoding='utf-8-sig')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    # Remove BOM and any leading/trailing whitespace
    content = content.lstrip('\ufeff')

    # Helper to extract a simple field (value until newline)
    def get_field(key: str) -> str:
        pattern = rf'^{re.escape(key)}:\s*(.*?)$'
        match = re.search(pattern, content, re.MULTILINE)
        return match.group(1).strip() if match else ''

    # Helper to extract a multiline field (until next field at start of line or end of block)
    def get_multiline_field(key: str) -> str:
        pattern = rf'^{re.escape(key)}:\s*(.*?)(?=^\w+:|```|\Z)'
        match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if not match:
            return ''
        value = match.group(1).strip()
        # Remove trailing triple backticks if present
        value = re.sub(r'\n```\s*$', '', value)
        return value

    # Helper to extract a list (bullets) under a key
    def get_list_field(key: str) -> List[str]:
        block = get_multiline_field(key)
        if not block:
            return []
        items = []
        for line in block.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                items.append(line[2:].strip())
            elif line and items and not line.startswith('#'):
                # Continuation of previous item
                items[-1] += ' ' + line
        return items

    # Basic fields
    paper_id = get_field('paper_id')
    designation = get_field('designation')
    title = get_field('title')
    authors = get_field('authors')
    year_str = get_field('year')
    year = int(year_str) if year_str.isdigit() else 0
    venue = get_field('venue')
    tldr = get_multiline_field('tldr') or get_field('tldr')
    problem_and_motivation = get_multiline_field('problem_and_motivation')
    findings = get_list_field('findings')
    limitations = get_list_field('limitations')
    remember_this = get_list_field('remember_this')
    
    # Approach is a list
    approach = get_list_field('approach')
    
    # Odin topics (list)
    topics_block = get_multiline_field('odin_topics')
    odin_topics = []
    if topics_block:
        for line in topics_block.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                odin_topics.append(line[2:].strip())
            elif line and not line.startswith('#') and ',' in line:
                # Possibly inline comma-separated
                odin_topics.extend([t.strip() for t in line.split(',') if t.strip()])

    # Directly justifies (nested inside relevance)
    justifies_block = get_multiline_field('directly_justifies')
    directly_justifies = []
    if justifies_block:
        for line in justifies_block.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                directly_justifies.append(line[2:].strip())

    # Build the same dict structure as before
    return {
        'paper_id': paper_id or 'No ID',
        'designation': designation or 'unknown',
        'title': title or file_path.stem,
        'authors': authors or 'Unknown',
        'year': year,
        'venue': venue or 'Unknown',
        'odin_topics': odin_topics,
        'tldr': tldr or '',
        'problem_and_motivation': problem_and_motivation or '',
        'approach': approach,
        'findings': findings,
        'limitations': limitations,
        'remember_this': remember_this,
        'relevance': {
            'directly_justifies': directly_justifies
        }
    }

def paper_matches_subtopic(paper: Dict[str, Any], subtopic: str) -> bool:
    topics = paper.get('odin_topics', [])
    return subtopic in topics

def file_matches_prefix(file_path: Path, prefix: str) -> bool:
    return file_path.name.startswith(prefix)

def truncate_list(lst: List[str], max_items: int = 3) -> List[str]:
    if not lst:
        return []
    return lst[:max_items]

def format_markdown_entry(paper: Dict[str, Any], filename: str, parse_error: bool = False) -> str:
    if parse_error:
        md = f"\n## ⚠️ [PARSING FAILED] {filename}\n"
        md += f"**Filename:** `{filename}`  \n"
        md += "**Status:** Could not extract YAML from this file. The summary may be malformed or missing a YAML code block.\n"
        md += "**Action:** Please check the original file or ask the user to provide a corrected version.\n"
        md += "---\n"
        return md

    title = paper.get('title', 'Unknown Title')
    authors = paper.get('authors', 'Unknown')
    year = paper.get('year', 0)
    paper_id = paper.get('paper_id', 'No ID')
    tldr = paper.get('tldr', 'No TLDR provided.')
    problem = paper.get('problem_and_motivation', 'Not specified.')
    approach_list = paper.get('approach', [])
    findings_list = paper.get('findings', [])
    limitations_list = paper.get('limitations', [])
    directly_justifies = paper.get('relevance', {}).get('directly_justifies', [])
    odin_topics = paper.get('odin_topics', [])
    remember = paper.get('remember_this', [])

    md = f"\n## {title}\n"
    md += f"**Filename:** `{filename}`  \n"
    md += f"**Authors:** {authors} ({year})  \n"
    md += f"**ID:** `{paper_id}`  \n"
    md += f"**Odin Topics:** {', '.join(odin_topics) if odin_topics else 'None'}  \n\n"

    md += f"**TLDR:** {tldr}\n\n"
    md += f"**Problem & Motivation:** {problem}\n\n"

    if approach_list:
        md += "**Approach (summary):**\n"
        for item in truncate_list(approach_list, 3):
            md += f"- {item}\n"
        md += "\n"

    if findings_list:
        md += "**Key Findings (selected):**\n"
        for f in truncate_list(findings_list, 4):
            md += f"- {f}\n"
        md += "\n"

    if directly_justifies:
        md += "**Supports Odin (direct justifications):**\n"
        for claim in truncate_list(directly_justifies, 3):
            md += f"- {claim}\n"
        md += "\n"

    if limitations_list:
        md += "**Limitations / Contradictions for Odin:**\n"
        for lim in truncate_list(limitations_list, 3):
            md += f"- {lim}\n"
        md += "\n"

    if remember:
        md += "**Key takeaways:**\n"
        for item in truncate_list(remember, 3):
            md += f"- {item}\n"
        md += "\n"

    md += "---\n"
    return md

def main():
    parser = argparse.ArgumentParser(
        description="Compile summary reports by subtopic OR filename prefix.\n"
                    "Prefix mode includes all matching files even if YAML parsing fails."
    )
    parser.add_argument('--folder', '-f', help='Folder containing .md summary files (auto-detects folder with "Summaries" if omitted)')
    parser.add_argument('--subtopic', '-s', help='Subtopic code (e.g., "1.A")')
    parser.add_argument('--prefix', '-p', help='Filename prefix (e.g., "L--", "I--", "LA--")')
    parser.add_argument('--output', '-o', help='Output Markdown file name (relative to 00_Reports/)')
    args = parser.parse_args()

    if not args.subtopic and not args.prefix:
        print("Error: You must provide either --subtopic or --prefix.")
        return
    if args.subtopic and args.prefix:
        print("Error: Cannot use both --subtopic and --prefix. Choose one.")
        return

    if args.folder:
        folder = Path(args.folder)
        if not folder.is_dir():
            print(f"Error: {folder} is not a directory")
            return
    else:
        try:
            folder = find_summaries_folder()
            print(f"Auto-detected folder: {folder}")
        except FileNotFoundError as e:
            print(e)
            return

    reports_dir = Path("00_Reports")
    reports_dir.mkdir(exist_ok=True)

    md_files = list(folder.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {folder}")
        return

    matched = []  # list of (filename, paper_dict, parse_error_flag)

    if args.subtopic:
        subtopic = args.subtopic.strip()
        for f in md_files:
            paper_dict = extract_fields_from_md(f)
            if paper_dict and paper_matches_subtopic(paper_dict, subtopic):
                matched.append((f.name, paper_dict, False))
            elif paper_dict:
                # File parsed but topics don't match – skip silently
                pass
            else:
                # Parsing failed – skip (cannot verify subtopic)
                print(f"Skipping {f.name} (no valid YAML) for subtopic mode")
        if not matched:
            print(f"No papers found for subtopic '{subtopic}'")
            return
        if args.output:
            output_path = reports_dir / args.output
        else:
            safe = subtopic.replace('.', '_')
            output_path = reports_dir / f"{safe}_Comprehensive_Report.md"
        title_line = f"# Comprehensive Report for Subtopic: `{subtopic}`"
    else:  # prefix mode – never skip
        prefix = args.prefix.strip()
        for f in md_files:
            if not file_matches_prefix(f, prefix):
                continue
            paper_dict = extract_fields_from_md(f)
            if paper_dict:
                matched.append((f.name, paper_dict, False))
            else:
                # Include with error placeholder
                matched.append((f.name, None, True))
                print(f"Including {f.name} despite parsing failure (prefix mode)")
        if not matched:
            print(f"No files found with prefix '{prefix}'")
            return
        if args.output:
            output_path = reports_dir / args.output
        else:
            safe_prefix = prefix.replace('--', '_').replace('-', '_')
            output_path = reports_dir / f"{safe_prefix}_Comprehensive_Report.md"
        title_line = f"# Comprehensive Report for Prefix: `{prefix}`"

    # Sort: papers with valid YAML first by year, then errors at the end
    def sort_key(item):
        _, paper_dict, has_error = item
        if has_error:
            return (-1, 0)  # errors go last
        return (0, -paper_dict.get('year', 0)) if paper_dict else (0, 0)
    matched.sort(key=sort_key)

    report_lines = [title_line, "", f"**Total files:** {len(matched)}", "",
                    "This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.",
                    "", "---", ""]

    for filename, paper_dict, has_error in matched:
        report_lines.append(format_markdown_entry(paper_dict or {}, filename, has_error))

    report_lines.append("")
    report_lines.append("## Note for the Agent")
    report_lines.append("")
    report_lines.append("The summaries above contain **essential extracts** – enough to understand each paper's relevance to Odin, including supporting evidence and limitations.")
    report_lines.append("If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),")
    report_lines.append("**ask the user to send the original summary file (`<filename>_summarized.md`) or the converted MarkItDown file(`<filename>_marked.md`)** for the specific paper(s) of interest.")
    report_lines.append("Do not invent missing information. Acknowledge gaps when they exist.")

    output_path.write_text("\n".join(report_lines), encoding='utf-8')
    print(f"✅ Compiled {len(matched)} papers into '{output_path}'")

if __name__ == "__main__":
    main()