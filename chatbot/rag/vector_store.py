
import os
import shutil
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from portfolio.settings import BASE_DIR

VECTOR_STORE_PATH = os.path.join(BASE_DIR, "chatbot", "rag", "vector_store")

def build_vector_store():
    # Import heavy document loaders only when rebuilding to keep default imports light
    from chatbot.rag.loaders.pdf_loader import load_pdfs
    from chatbot.rag.loaders.txt_loader import load_txt_and_md
    from chatbot.rag.loaders.code_loader import load_py

    print("Loading documents...")
    documents = load_pdfs() + load_txt_and_md() + load_py()
    print(f"Loaded {len(documents)} documents.")

    if not documents:
        print("No documents to index.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if os.path.exists(VECTOR_STORE_PATH):
        shutil.rmtree(VECTOR_STORE_PATH)

    print("Building vector store...")
    vector_store = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=VECTOR_STORE_PATH
    )
    vector_store.persist()
    print("Vector store built successfully.")


def get_vector_store():
    if not os.path.exists(VECTOR_STORE_PATH):
        build_vector_store()
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=VECTOR_STORE_PATH, embedding_function=embeddings)
