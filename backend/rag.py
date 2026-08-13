rom sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from pypdf import PdfReader
f
# Load embedding model only once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
chunks = []

def read_pdf(pdf_path):
    """
    Reads a PDF and returns all its text as a single string.
    """
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def chunk_text(text, chunk_size=500, overlap=100):
    """
    Splits text into overlapping chunks.
    """
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks