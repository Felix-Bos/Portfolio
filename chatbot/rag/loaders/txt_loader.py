
import os
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document
from portfolio.settings import BASE_DIR

def load_txt_and_md():
    data_path = os.path.join(BASE_DIR, "data")
    documents = []
    for root, _, files in os.walk(data_path):
        for file in files:
            if file.endswith(".txt") or file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    loader = TextLoader(file_path, encoding='utf-8')
                    documents.extend(loader.load())
                except Exception as e:
                    print(f"Error loading text file {file_path}: {e}")
    return documents
