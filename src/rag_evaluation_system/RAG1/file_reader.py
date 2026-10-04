from pymupdf import open
import re
from typing import List
from pathlib import Path


def extract_paragraph(pdf_path: str | Path) -> List[str]:
    """Extracts paragraphs from a PDF file."""
    doc = open(pdf_path)
    paragraphs = []

    for page in doc:
        blocks = page.get_text("blocks")
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))

        for block in blocks:
            text = block[4]
            text = re.sub(r"\s+", " ", text).strip()
            if text:
                paragraphs.append(text)
    return paragraphs


# print(extract_paragraph("src/rag_evaluation_system/pdfs/Penguins_ACL.pdf"))
