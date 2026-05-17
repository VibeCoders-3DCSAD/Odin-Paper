#!/usr/bin/env python3
"""
PDF Registry Builder (with central registry storage)

Usage: python registrify.py <target_directory>

Scans the target directory for PDF files, converts each to Markdown
(via the markitdown package), creates an empty summary file, and builds a registry
saved as <target_directory>_Registry.md inside the ./00_Registries folder.
"""

import os
import sys
import glob
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    raise ImportError("The 'markitdown' package is required. Install it with: pip install markitdown")

def get_directory_name(path: str) -> str:
    """Return the base name of the given directory path."""
    return os.path.basename(os.path.abspath(path))

def find_pdfs(directory: str) -> list:
    """Return a list of PDF file paths in the given directory."""
    pattern = os.path.join(directory, "*.pdf")
    return glob.glob(pattern)

def convert_pdf_to_markdown(pdf_path: str, output_md_path: str) -> None:
    """
    Convert a PDF file to Markdown using MarkItDown and write to output_md_path.
    """
    md_converter = MarkItDown()
    result = md_converter.convert(pdf_path)
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(result.text_content)

def create_empty_summary(directory: str, pdf_stem: str) -> None:
    """Create an empty <pdf-stem>_summarized.md file inside the target directory."""
    summary_path = os.path.join(directory, f"{pdf_stem}_summarized.md")
    Path(summary_path).touch()

def build_registry_content(pdf_stems: list, dir_name: str) -> str:
    """
    Build the content for the registry.
    Each PDF gets a section with a placeholder for description only.
    """
    lines = [
        f"# Topic Registry - {dir_name}",
        "",
        "---",
        ""
    ]
    for i, stem in enumerate(pdf_stems):
        lines.append(f"## {stem}")
        lines.append("")
        lines.append("### Description")
        lines.append("")
        lines.append("[description]")
        lines.append("")
        # Add separator between sections, but not after the last one
        if i != len(pdf_stems) - 1:
            lines.append("---")
            lines.append("")
    return "\n".join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python registrify.py <target_directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print(f"Error: '{target_dir}' is not a valid directory.")
        sys.exit(1)

    # Resolve to absolute path for clarity
    target_dir = os.path.abspath(target_dir)
    dir_name = get_directory_name(target_dir)
    pdf_files = find_pdfs(target_dir)

    # Determine the central registries folder (same level as this script)
    script_dir = Path(__file__).parent.resolve()
    registries_dir = script_dir / "00_Registries"
    registries_dir.mkdir(exist_ok=True)

    if not pdf_files:
        print(f"No PDF files found in '{target_dir}'.")
        # Still create a registry with a "no PDFs" message
        registry_content = f"# Topic Registry - {dir_name}\n\n---\n\nNo PDF files found."
        registry_path = registries_dir / f"{dir_name}_Registry.md"
        with open(registry_path, "w", encoding="utf-8") as reg:
            reg.write(registry_content)
        print(f"Registry created (no PDFs): {registry_path}")
        return

    pdf_stems = []
    for pdf_path in pdf_files:
        # Get filename without extension
        stem = Path(pdf_path).stem
        pdf_stems.append(stem)

        # Create the _marked.md file inside the target directory
        marked_path = os.path.join(target_dir, f"{stem}_marked.md")
        print(f"Converting: {pdf_path} -> {marked_path}")
        try:
            convert_pdf_to_markdown(pdf_path, marked_path)
        except Exception as e:
            print(f"Error converting {pdf_path}: {e}")

        # Create the empty _summarized.md file inside the target directory
        create_empty_summary(target_dir, stem)
        print(f"Created empty summary: {os.path.join(target_dir, stem + '_summarized.md')}")

    # Build the registry content and save it inside 00_Registries
    registry_content = build_registry_content(pdf_stems, dir_name)
    registry_path = registries_dir / f"{dir_name}_Registry.md"
    with open(registry_path, "w", encoding="utf-8") as reg:
        reg.write(registry_content)
    print(f"Registry saved to: {registry_path}")

if __name__ == "__main__":
    main()