from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vectorstore = FAISS.load_local(
    "app/vectorstore/company_index",
    embeddings,
    allow_dangerous_deserialization=True
)


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}
)


def retrieve_company_context(query: str):

    docs = retriever.invoke(query)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    return context