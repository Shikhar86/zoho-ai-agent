from app.services.file_loader import load_text

knowledge_files = {
    "refund": "refund.txt",
    "pricing": "pricing.txt",
    "support": "support.txt",
    "meeting": "meeting.txt"
}


def search_company_documents(email_body):

    email = email_body.lower()

    for keyword, filename in knowledge_files.items():

        if keyword in email:
            return load_text(filename)

    return load_text("no_company_info.txt")