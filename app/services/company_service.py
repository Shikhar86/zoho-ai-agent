from app.repositories.company_repository import get_company_document


def get_company_context(email_body):

    email = email_body.lower()

    if "refund" in email:
        return get_company_document("refund.txt")

    elif "pricing" in email:
        return get_company_document("pricing.txt")

    elif "support" in email:
        return get_company_document("support.txt")

    return get_company_document("no_company_info.txt")