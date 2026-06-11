#!/usr/bin/env python3
"""
Compile comprehensive reports for a subtopic from .md files containing ```yaml blocks.
Saves output to ./00_Reports/ by default.
Includes filename, problem/motivation, approach, findings, support for Odin, and limitations.
"""

import argparse
import re
import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional

def find_summaries_folder() -> Path:
    cwd = Path.cwd()
    matches = [p for p in cwd.rglob("*") if p.is_dir() and "summaries" in p.name.lower()]
    if not matches:
        raise FileNotFoundError("No --folder provided and no folder containing 'Summaries' found.")
    matches.sort(key=lambda p: len(p.relative_to(cwd).parts))
    return matches[0]

def extract_yaml_from_md(file_path: Path) -> Optional[Dict[str, Any]]:
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    pattern = re.compile(r'```yaml\s*\n(.*?)\n```', re.DOTALL)
    match = pattern.search(content)
    if not match:
        pattern2 = re.compile(r'```\s*\n(.*?)\n```', re.DOTALL)
        match = pattern2.search(content)
    if not match:
        print(f"No YAML code block found in {file_path}")
        return None

    yaml_str = match.group(1).strip()
    if not yaml_str:
        print(f"Empty YAML block in {file_path}")
        return None

    try:
        data = yaml.safe_load(yaml_str)
        if not isinstance(data, dict):
            print(f"YAML block in {file_path} did not produce a dict")
            return None
        return data
    except yaml.YAMLError as e:
        print(f"YAML parsing error in {file_path}:\n{e}")
        return None

def paper_matches_subtopic(paper: Dict[str, Any], subtopic: str) -> bool:
    topics = paper.get('odin_topics', [])
    return subtopic in topics

def truncate_list(lst: List[str], max_items: int = 3) -> List[str]:
    if not lst:
        return []
    return lst[:max_items]

def format_markdown_entry(paper: Dict[str, Any], filename: str) -> str:
    """Generate a detailed markdown section for one paper (without critical citations etc.)."""
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
    # remember_this still useful
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
        md += "**✅ Supports Odin (direct justifications):**\n"
        for claim in truncate_list(directly_justifies, 3):
            md += f"- {claim}\n"
        md += "\n"

    if limitations_list:
        md += "**⚠️ Limitations / Contradictions for Odin:**\n"
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', '-f', help='Folder containing .md summary files')
    parser.add_argument('--subtopic', '-s', required=True, help='Subtopic code (e.g., "1.A")')
    parser.add_argument('--output', '-o', help='Output Markdown file (relative to 00_Reports/)')
    args = parser.parse_args()

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

    subtopic = args.subtopic.strip()
    
    # Create reports directory
    reports_dir = Path("00_Reports")
    reports_dir.mkdir(exist_ok=True)
    
    if args.output:
        output_path = reports_dir / args.output
    else:
        safe_subtopic = subtopic.replace('.', '_')
        output_path = reports_dir / f"{safe_subtopic}_Comprehensive_Report.md"

    md_files = list(folder.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {folder}")
        return

    papers = []
    for f in md_files:
        paper_dict = extract_yaml_from_md(f)
        if paper_dict and paper_matches_subtopic(paper_dict, subtopic):
            papers.append((f.name, paper_dict))

    if not papers:
        print(f"No papers found for subtopic '{subtopic}'")
        return

    papers.sort(key=lambda x: x[1].get('year', 0), reverse=True)

    report_lines = [
        f"# Comprehensive Report for Subtopic: `{subtopic}`",
        "",
        f"**Total relevant papers:** {len(papers)}",
        "",
        "This report includes problem/motivation, approach, key findings, support for Odin, and limitations/contradictions.",
        "",
        "---",
        ""
    ]

    for filename, paper in papers:
        report_lines.append(format_markdown_entry(paper, filename))

    report_lines.append("")
    report_lines.append("## 📌 Note for the Agent")
    report_lines.append("")
    report_lines.append("The summaries above contain **essential extracts** – enough to understand the paper's relevance to Odin, including supporting evidence and limitations.")
    report_lines.append("If you need additional details not shown here (e.g., **critical citations, definitions, equations, full methodology, or the complete mapping rationale**),")
    report_lines.append("**ask the user to send the original summary file (`.md`)** for the specific paper(s) of interest.")
    report_lines.append("Do not invent missing information. Acknowledge gaps when they exist.")

    output_path.write_text("\n".join(report_lines), encoding='utf-8')
    print(f"✅ Compiled {len(papers)} papers into '{output_path}'")

if __name__ == "__main__":
    main()