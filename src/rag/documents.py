"""
MILESTONE 2 - Document Processing
----------------------------------
Load PDF / TXT / DOCX  ->  clean the text  ->  cut it into chunks.
"""
import os
import re

from pypdf import PdfReader


def load_document(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if ext == ".txt":
        with open(path, encoding="utf-8") as f:
            return f.read()

    if ext == ".docx":
        from docx import Document
        return "\n\n".join(p.text for p in Document(path).paragraphs)

    raise ValueError(f"Unsupported file type: {ext}")


def clean_text(text):
    text = re.sub(r"(\w+)-\n(\w+)", r"\1\2", text)   # join "safe-\nty" -> "safety"
    text = re.sub(r"[ \t]+", " ", text)               # extra spaces
    text = re.sub(r"(?m)^\s*\d+\s*$", "", text)       # lines that are only page numbers
    text = re.sub(r"\n{3,}", "\n\n", text)            # too many blank lines
    return text.strip()


def make_chunks(text, size=500, overlap=50):
    """
    Split by paragraph first.
    If a paragraph is too long, split it by words.
    """

    chunks = []

    for para in re.split(r"\n{2,}", text):
        para = para.strip()

        if not para:
            continue

        if len(para) <= size:
            chunks.append(para)
            continue

        words = para.split()
        current = ""

        for word in words:
            if len(current) + len(word) + 1 <= size:
                current += (" " if current else "") + word
            else:
                chunks.append(current)
                current = word

        if current:
            chunks.append(current)

    return chunks

def process_file(path):
    """Full pipeline: file -> list of clean chunks."""
    return make_chunks(clean_text(load_document(path)))


if __name__ == "__main__":
    chunks = process_file("data/safety_manual.pdf")
    print(len(chunks), "chunks")
    for i,chunk in enumerate(chunks):
        print(f"\n--Chunk{i}--")
        print(chunk)
