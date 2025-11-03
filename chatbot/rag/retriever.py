
from chatbot.rag.vector_store import get_vector_store

def retrieve_context(query, k=4):
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": k})
    documents = retriever.invoke(query)
    print(f"Retrieved {len(documents)} documents:")
    for doc in documents:
        print(doc.metadata)
    context = "\n".join([doc.page_content for doc in documents])
    print(f"Context: {context[:500]}...")
    return context
