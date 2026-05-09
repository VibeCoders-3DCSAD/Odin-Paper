import os
import sys
from pathlib import Path
from Markitdown.packages.markitdown.src.markitdown import MarkItDown  # new import

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
    
    # Initialize MarkItDown once
    md_converter = MarkItDown()
    
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        
        md1_path = folder / f"{base_name}.md"
        md2_path = folder / f"{base_name}_summarized.md"
        
        created = []
        skipped = []
        
        # Handle <paper_name>.md - convert PDF to Markdown only if missing
        if not md1_path.exists():
            try:
                print(f"  Converting {pdf_path.name} to Markdown...")
                result = md_converter.convert(str(pdf_path))
                with open(md1_path, 'w', encoding='utf-8') as f:
                    f.write(result.text_content)
                created.append(md1_path.name)
            except Exception as e:
                print(f"  ✗ Conversion failed for {pdf_path.name}: {e}")
                # Don't add to created or skipped, just report error
        else:
            skipped.append(md1_path.name)
        
        # Handle <paper_name>_summarized.md - create empty if missing
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