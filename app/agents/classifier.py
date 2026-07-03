from app.services.llm import llm


def classify_email(state):

    prompt = f"""
    Classify this email.

    Email:
    {state["email_body"]}

    Categories:
    MEETING
    SALES
    SUPPORT
    FOLLOWUP
    OTHER

    Return ONLY the category.
    """

    result = llm.invoke(prompt)

    return {
        "email_type": result.content.strip()
    }