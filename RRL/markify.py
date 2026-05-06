import os
import sys
from pathlib import Path

def markify(folder_path):
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    pdf_files = list(folder.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{folder_path}'")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s)\n")
    
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        
        md1_path = folder / f"{base_name}.md"
        md2_path = folder / f"{base_name}_summarized.md"
        
        created = []
        skipped = []
        
        if not md1_path.exists():
            md1_path.touch()
            created.append(md1_path.name)
        else:
            skipped.append(md1_path.name)
            
        if not md2_path.exists():
            md2_path.touch()
            created.append(md2_path.name)
        else:
            skipped.append(md2_path.name)
        
        if created:
            print(f"✓ Created: {', '.join(created)}")
        if skipped:
            print(f"⚠ Skipped (already exist): {', '.join(skipped)}")
        print(f"  For: {pdf_path.name}\n")

if __name__ == "__main__":
    # Use command-line argument if provided, otherwise use current directory
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = "."
    
    markify(folder_path)