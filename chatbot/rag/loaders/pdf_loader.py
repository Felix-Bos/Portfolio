
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
from portfolio.settings import BASE_DIR

def load_pdfs():
    data_path = os.path.join(BASE_DIR, "data")
    documents = []
    for root, _, files in os.walk(data_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    loader = PyPDFLoader(file_path)
                    documents.extend(loader.load_and_split())
                except Exception as e:
                    print(f"Error loading PDF file {file_path}: {e}")
    return documents
