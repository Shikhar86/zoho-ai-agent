from app.services.llm import text_llm


def write_reply(state):

    print("WRITER AGENT EXECUTED")

    prompt = f"""
You are an AI email assistant.

Your job is to write a professional email reply.

==========================
ORIGINAL EMAIL
==========================

Subject:
{state["email_subject"]}

Body:
{state["email_body"]}


==========================
MEMORY CONTEXT
==========================

{state.get("memory_context", "")}


==========================
COMPANY CONTEXT
==========================

{state.get("company_context", "")}


==========================
INTERNET CONTEXT
==========================

{state.get("internet_context", "")}


==========================
IMPORTANT RULES
==========================

1. Read the original email carefully.

2. Use ONLY the context that is relevant to the user's question.

3. Ignore any context that is unrelated.

4. Never combine unrelated information.

5. Never invent facts.

6. If the answer is not present in any context, politely say you do not have enough information.

7. If Memory Context answers the question, prioritize it.

8. Use Company Context only for company policies, pricing, support, products or internal information.

9. Use Internet Context only for current events or external facts.

10. Write a natural professional email.

11. Do NOT mention "Memory Context", "Company Context", or "Internet Context".

12. Return ONLY the email.

Do NOT return JSON.

Do NOT return markdown.

Do NOT explain your reasoning.
"""

    response = text_llm.invoke(prompt)

    state["draft_reply"] = response.content

    print("\n===== DRAFT REPLY =====")
    print(state["draft_reply"])

    return state