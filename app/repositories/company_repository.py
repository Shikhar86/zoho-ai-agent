from app.vectorstore.retriever import retrieve_company_context


def search_company_documents(email_body):

    return retrieve_company_context(email_body)