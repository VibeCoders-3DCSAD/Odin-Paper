import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Move PDFs from selected folders into '01_Papers'.\n"
                    "Folders starting with '0' are NEVER processed."
    )
    parser.add_argument(
        "--prefix",
        default="",
        help="Only process directories whose name starts with this string (e.g., 'A' or '1').\n"
             "Cannot be '0' or start with '0'."
    )
    args = parser.parse_args()

    # Safety: refuse to process 0‑prefixed folders at all
    if args.prefix and args.prefix.startswith("0"):
        print("ERROR: --prefix cannot start with '0' because 0‑prefixed folders are forbidden.")
        return

    current_dir = Path.cwd()
    target_dir = current_dir / "01_Papers"
    target_dir.mkdir(exist_ok=True)

    for folder in current_dir.iterdir():
        if not folder.is_dir():
            continue
        if folder == target_dir:
            continue

        # BLOCK any folder starting with '0'
        if folder.name.startswith("0"):
            print(f"INFO: Skipping folder '{folder.name}' (starts with '0')")
            continue

        # Apply user‑defined prefix filter
        if args.prefix and not folder.name.startswith(args.prefix):
            continue

        # Move all PDFs recursively from allowed folders
        for pdf_file in folder.rglob("*.pdf"):
            dest = target_dir / pdf_file.name
            print(f"Moving: {pdf_file} -> {dest}")
            shutil.move(str(pdf_file), str(dest))

if __name__ == "__main__":
    main()