from app.services.llm import text_llm


def write_reply(state):

    print("WRITER AGENT EXECUTED")

    prompt = f"""
You are a professional email assistant.

Write a complete email reply.

Original Email

Subject:
{state["email_subject"]}

Body:
{state["email_body"]}

Company Context:
{state.get("company_context", "")}

Internet Context:
{state.get("internet_context", "")}

Memory Context:
{state.get("memory_context", "")}

Instructions:

- Use the company context if available.
- Use the internet context if available.
- Use the memory context if available.
- Be polite.
- Answer every question.
- Write a complete email.

Return ONLY the email.

Do NOT return JSON.
Do NOT return markdown.
Do NOT return only a subject.
"""

    response = text_llm.invoke(prompt)

    state["draft_reply"] = response.content

    print("\n===== DRAFT REPLY =====")
    print(state["draft_reply"])

    return state