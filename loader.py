import pdfplumber
import fitz  # PyMuPDF
import os
import shutil
from pathlib import Path
from langchain.schema import Document
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

def is_valid_table_cell(cell):
    return str(cell) if cell is not None else ""


def extract_from_pdf(
    pdf_path: str,
    image_output_dir: str = r"C:\Users\rudra\Desktop\Agentic_ai\Rag_Project\extracted_images"
) -> list[Document]:
    # 🧹 Clean old folder if exists
    if os.path.exists(image_output_dir):
        shutil.rmtree(image_output_dir)
    os.makedirs(image_output_dir, exist_ok=True)

    text_docs = []
    table_docs = []
    image_docs = []

    # === STEP 1: Text + Table Extraction using pdfplumber ===
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_number = i + 1

            # TEXT
            text = page.extract_text()
            if text:
                text_docs.append(Document(
                    page_content=text,
                    metadata={"page": page_number, "type": "text"}
                ))
                

            # TABLES
            tables = page.extract_tables()
            for table in tables:
                table_text = "\n".join([
                    " | ".join([is_valid_table_cell(cell) for cell in row])
                    for row in table if row
                ])
                table_docs.append(Document(
                    page_content=table_text,
                    metadata={"page": page_number, "type": "table"}
                ))

    # === STEP 2: Image Extraction using PyMuPDF ===
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for j, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(image_output_dir, f"page{page_num+1}_img{j}.{image_ext}")

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            # OCR extraction
            try:
                ocr_text = pytesseract.image_to_string(Image.open(image_path))
                if ocr_text.strip():
                    image_docs.append(Document(
                        page_content=ocr_text.strip(),
                        metadata={"page": page_num + 1, "type": "image"}
                    ))
            except Exception as e:
                print(f"⚠️ Error processing {image_path}: {e}")

    return text_docs + table_docs + image_docs
