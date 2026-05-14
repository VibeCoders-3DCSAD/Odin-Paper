# markify.py
# Converts all PDFs in the current directory to Markdown using MarkItDown.

import os
from pathlib import Path
from markitdown import MarkItDown

def markify():
    # Always use the current working directory
    folder = Path.cwd()
    
    pdf_files = list(folder.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{folder}'")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) in current directory\n")
    
    # Initialize MarkItDown once
    md_converter = MarkItDown()
    
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        
        md1_path = folder / f"{base_name}.md"
        md2_path = folder / f"{base_name}_summarized.md"
        
        try:
            print(f"  Converting {pdf_path.name} to Markdown...")
            result = md_converter.convert(str(pdf_path))
            with open(md1_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            print(f"  ✓ Overwrote: {md1_path.name}")
        except Exception as e:
            print(f"  ✗ Conversion failed for {pdf_path.name}: {e}")
        
        # Create/overwrite empty _summarized.md file (placeholder for later summarization)
        with open(md2_path, 'w', encoding='utf-8') as f:
            f.write("")
        print(f"  ✓ Created/overwrote: {md2_path.name}")
        
        print(f"  For: {pdf_path.name}\n")

if __name__ == "__main__":
    markify()