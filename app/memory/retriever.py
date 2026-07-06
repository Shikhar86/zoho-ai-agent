from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


# Load embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# Load Memory FAISS index
vectorstore = FAISS.load_local(
    "app/memory/memory_index",
    embeddings,
    allow_dangerous_deserialization=True
)


# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}
)


def retrieve_memory_context(query: str):
    """
    Retrieve the most relevant previous email conversation.
    """

    docs = retriever.invoke(query)

    return "\n\n".join(doc.page_content for doc in docs)