import shutil
from pathlib import Path

def main():
    current_dir = Path.cwd()
    target_dir = current_dir / "01_Papers"
    target_dir.mkdir(exist_ok=True)

    for folder in current_dir.iterdir():
        # Skip non‑directories and folders starting with '0'
        if not folder.is_dir() or folder.name.startswith("0"):
            continue

        # Find all PDF files recursively in this folder
        for pdf_file in folder.rglob("*.pdf"):
            dest = target_dir / pdf_file.name
            print(f"Moving: {pdf_file} -> {dest}")
            shutil.move(str(pdf_file), str(dest))

if __name__ == "__main__":
    main()