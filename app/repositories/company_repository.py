from app.services.file_loader import load_text


def get_company_document(document_name):

    return load_text(document_name)