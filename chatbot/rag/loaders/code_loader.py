
import os
import ast
from langchain.schema import Document
from portfolio.settings import BASE_DIR

def load_py():
    data_path = os.path.join(BASE_DIR, "data")
    documents = []
    for root, _, files in os.walk(data_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        # Extract docstrings
                        tree = ast.parse(content)
                        docstrings = [node.docstring for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)) and node.docstring]
                        # Extract comments
                        comments = [line.strip() for line in content.splitlines() if line.strip().startswith("#")]
                        
                        extracted_content = "\n".join(docstrings + comments)
                        if extracted_content:
                            documents.append(Document(page_content=extracted_content, metadata={"source": file_path}))

                except Exception as e:
                    print(f"Error loading Python file {file_path}: {e}")
    return documents
