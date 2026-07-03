from app.repositories.search_repository import search_web


def get_internet_context(email_body):

    response = search_web(email_body)

    results = response.get("results", [])

    if not results:
        return "No internet information found."

    context = ""

    for result in results:
        context += f"""
Title: {result.get("title")}

Content: {result.get("content")}

URL: {result.get("url")}

----------------------------
"""

    return context