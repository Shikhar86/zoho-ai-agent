from app.repositories.memory_repository import search_memory_documents


def get_memory_context(email_body):

    return search_memory_documents(email_body)