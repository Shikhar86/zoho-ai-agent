from app.memory.retriever import retrieve_memory_context


def search_memory_documents(email_body):

    return retrieve_memory_context(email_body)