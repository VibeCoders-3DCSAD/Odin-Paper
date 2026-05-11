import sys
import shutil
import argparse
from pathlib import Path

def organize_files(folder_path, move_pdf=True, move_plain_md=True, move_summarized=True, overwrite=False):
    """
    Moves files from the given folder into organized subdirectories.
    
    Args:
        folder_path: Source folder containing the files
        move_pdf: Move PDF files to ../01_Papers
        move_plain_md: Move non-summarized .md files to ../03_Related Literature
        move_summarized: Move *_summarized.md files to ../02_Reviews
        overwrite: If True, overwrite existing files; otherwise skip
    """
    source_dir = Path(folder_path).resolve()
    
    if not source_dir.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    # Define destination directories relative to source's parent
    parent = source_dir.parent
    papers_dir = parent / "01_Papers"
    reviews_dir = parent / "02_Reviews"
    related_dir = parent / "03_Related Literature"
    
    # Create destination directories only if needed
    if move_pdf:
        papers_dir.mkdir(exist_ok=True)
    if move_summarized:
        reviews_dir.mkdir(exist_ok=True)
    if move_plain_md:
        related_dir.mkdir(exist_ok=True)
    
    # Move PDF files
    if move_pdf:
        pdf_files = list(source_dir.glob("*.pdf"))
        if pdf_files:
            print(f"\n📄 Moving PDFs ({len(pdf_files)} files)...")
            for pdf in pdf_files:
                dest = papers_dir / pdf.name
                _move_file(pdf, dest, "PDF", overwrite)
        else:
            print("\n📄 No PDF files found.")
    
    # Move markdown files
    md_files = list(source_dir.glob("*.md"))
    if not md_files:
        print("\n📝 No markdown files found.")
    else:
        # Separate files into categories
        plain_files = []
        summarized_files = []
        ignored_files = []
        
        for md in md_files:
            if md.name == "0_summarizer.md":
                ignored_files.append(md)
            elif md.name.endswith("_summarized.md"):
                summarized_files.append(md)
            else:
                plain_files.append(md)
        
        # Move summarized markdowns
        if move_summarized and summarized_files:
            print(f"\n📝 Moving summarized markdowns ({len(summarized_files)} files) → 02_Reviews...")
            for md in summarized_files:
                dest = reviews_dir / md.name
                _move_file(md, dest, "Summarized markdown", overwrite)
        elif not move_summarized and summarized_files:
            print(f"\n⚠ Skipped moving {len(summarized_files)} summarized markdown(s) (flag not set).")
        
        # Move plain markdowns (conversions)
        if move_plain_md and plain_files:
            print(f"\n📝 Moving plain markdowns ({len(plain_files)} files) → 03_Related Literature...")
            for md in plain_files:
                dest = related_dir / md.name
                _move_file(md, dest, "Plain markdown", overwrite)
        elif not move_plain_md and plain_files:
            print(f"\n⚠ Skipped moving {len(plain_files)} plain markdown(s) (flag not set).")
        
        # Report ignored files (0_summarizer.md)
        if ignored_files:
            print(f"\n○ Ignored ({len(ignored_files)} file(s)): {', '.join(f.name for f in ignored_files)}")

def _move_file(src, dst, file_type, overwrite=False):
    """Move a file, optionally overwriting existing destination."""
    if dst.exists():
        if overwrite:
            print(f"  ⚠ Overwriting: {src.name} (existing file in {dst.parent.name}/ will be replaced)")
            dst.unlink()  # Remove existing file
        else:
            print(f"  ⚠ Skipped: {src.name} → already exists in {dst.parent.name}/ (use --overwrite to replace)")
            return
    shutil.move(str(src), str(dst))
    print(f"  ✓ Moved: {src.name} → {dst.parent.name}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organize PDFs and markdown files into categorized folders.",
        epilog="Examples:\n"
               "  python organize.py /path/to/folder                # Move all three categories\n"
               "  python organize.py /path/to/folder --pdf          # Move only PDFs\n"
               "  python organize.py /path/to/folder --plain        # Move only plain markdowns\n"
               "  python organize.py /path/to/folder --summarized   # Move only summarized markdowns\n"
               "  python organize.py /path/to/folder --pdf --plain  # Move PDFs and plain markdowns\n"
               "  python organize.py /path/to/folder --overwrite    # Replace existing files instead of skipping",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("folder", nargs="?", default=".",
                        help="Source folder (default: current directory)")
    parser.add_argument("--pdf", action="store_true",
                        help="Move PDF files to ../01_Papers")
    parser.add_argument("--plain", action="store_true",
                        help="Move plain .md files (conversions) to ../03_Related Literature")
    parser.add_argument("--summarized", action="store_true",
                        help="Move *_summarized.md files to ../02_Reviews")
    parser.add_argument("--all", action="store_true",
                        help="Move all categories (same as default behavior)")
    parser.add_argument("--overwrite", action="store_true",
                        help="Overwrite existing files instead of skipping them")
    
    args = parser.parse_args()
    
    # Determine which categories to move
    # If no specific flags and not --all, default to all three
    if args.all or (not args.pdf and not args.plain and not args.summarized):
        move_pdf = True
        move_plain = True
        move_summarized = True
    else:
        move_pdf = args.pdf
        move_plain = args.plain
        move_summarized = args.summarized
    
    # Show what will be moved
    print("\n📁 Configuration:")
    print(f"   Source: {Path(args.folder).resolve()}")
    print(f"   Move PDFs: {'✓' if move_pdf else '✗'}")
    print(f"   Move plain markdowns: {'✓' if move_plain else '✗'}")
    print(f"   Move summarized markdowns: {'✓' if move_summarized else '✗'}")
    print(f"   Overwrite existing files: {'✓' if args.overwrite else '✗'}")
    print()
    
    organize_files(args.folder, move_pdf, move_plain, move_summarized, args.overwrite)