#!/usr/bin/env python3
"""
Strictly organize PDFs, conversions, and summaries from the current directory
into sibling folders.

Usage: python organize_refs.py

Run this script from inside the 04_Processing folder.
Files in the current directory (04_Processing) matching the patterns are moved to:
    ../01_Papers/          for PDFs
    ../02_Summaries/       for *_summarized.md
    ../03_Conversions/     for *_marked.md

Everything else (subdirectories, other file types) is ignored.
"""

import shutil
from pathlib import Path

def main():
    current_dir = Path.cwd()
    parent_dir = current_dir.parent

    # Destination folders (siblings of current_dir)
    papers_dir = parent_dir / "01_Papers"
    summaries_dir = parent_dir / "02_Summaries"
    conversions_dir = parent_dir / "03_Conversions"

    papers_dir.mkdir(exist_ok=True)
    summaries_dir.mkdir(exist_ok=True)
    conversions_dir.mkdir(exist_ok=True)

    pdf_moved = 0
    marked_moved = 0
    summarized_moved = 0

    # Process files directly inside the current directory, not subdirectories
    for file_path in current_dir.glob("*"):
        if not file_path.is_file():
            # Skip subdirectories
            continue

        # PDFs
        if file_path.suffix.lower() == ".pdf":
            dest = papers_dir / file_path.name
            print(f"Moving PDF: {file_path.name} -> ../01_Papers/")
            shutil.move(str(file_path), str(dest))
            pdf_moved += 1

        # Marked conversions (strict suffix _marked.md)
        elif file_path.name.endswith("_marked.md"):
            dest = conversions_dir / file_path.name
            print(f"Moving Marked: {file_path.name} -> ../03_Conversions/")
            shutil.move(str(file_path), str(dest))
            marked_moved += 1

        # Summaries (strict suffix _summarized.md)
        elif file_path.name.endswith("_summarized.md"):
            dest = summaries_dir / file_path.name
            print(f"Moving Summary: {file_path.name} -> ../02_Summaries/")
            shutil.move(str(file_path), str(dest))
            summarized_moved += 1

        # Anything else is silently ignored

    print("\n--- Summary ---")
    print(f"PDFs moved to ../01_Papers: {pdf_moved}")
    print(f"Marked conversions moved to ../03_Conversions: {marked_moved}")
    print(f"Summaries moved to ../02_Summaries: {summarized_moved}")


if __name__ == "__main__":
    main()