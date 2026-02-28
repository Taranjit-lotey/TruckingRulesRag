import pdfplumber
import os
from pathlib import Path


def parse_pdf(file_path: str) -> str:
    """Extract all text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def parse_all_pdfs(raw_dir: str) -> list[dict]:
    """Parse all PDFs in a directory. Returns a list of {filename, text} dicts."""
    documents = []
    pdf_files = list(Path(raw_dir).glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in {raw_dir}")
        return documents

    for pdf_path in pdf_files:
        print(f"Parsing: {pdf_path.name}")
        text = parse_pdf(str(pdf_path))
        if text:
            documents.append({
                "filename": pdf_path.name,
                "text": text,
                "source": str(pdf_path)
            })
        else:
            print(f"  Warning: No text extracted from {pdf_path.name}")

    print(f"Parsed {len(documents)} PDF(s) successfully.")
    return documents
