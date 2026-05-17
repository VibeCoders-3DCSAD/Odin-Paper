import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Move PDFs from selected folders into '01_Papers'."
    )
    parser.add_argument(
        "--prefix",
        default="",
        help="Only process directories whose name starts with this string (e.g., 'A' or '1')."
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=["00_Processing", "00_Registries"],
        help="Folder names to skip (even if they match the prefix)."
    )
    args = parser.parse_args()

    current_dir = Path.cwd()
    target_dir = current_dir / "01_Papers"
    target_dir.mkdir(exist_ok=True)

    for folder in current_dir.iterdir():
        # Must be a directory
        if not folder.is_dir():
            continue

        # Skip target folder itself
        if folder == target_dir:
            continue

        # Skip if name is in the exclude list
        if folder.name in args.exclude:
            continue

        # Only include folders that start with the given prefix
        if args.prefix and not folder.name.startswith(args.prefix):
            continue

        # Move all PDFs recursively from this folder
        for pdf_file in folder.rglob("*.pdf"):
            dest = target_dir / pdf_file.name
            print(f"Moving: {pdf_file} -> {dest}")
            shutil.move(str(pdf_file), str(dest))

if __name__ == "__main__":
    main()