from app.repositories.company_repository import search_company_documents


def get_company_context(email_body):

    return search_company_documents(email_body)