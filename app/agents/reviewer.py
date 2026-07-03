from app.services.llm import text_llm


def review_reply(state):

    print("REVIEWER AGENT EXECUTED")

    prompt = f"""
You are a senior customer support manager.

Review the following email reply.

Original Email

Subject:
{state["email_subject"]}

Body:
{state["email_body"]}


Draft Reply

{state["draft_reply"]}


Your job:

- Fix grammar.
- Fix spelling.
- Improve professionalism.
- Improve politeness.
- Make sure every question is answered.
- Keep the meaning the same.

If the email is already excellent,
return it unchanged.

Return ONLY the final email.

Do NOT return JSON.
Do NOT explain your changes.
"""

    response = text_llm.invoke(prompt)

    state["final_reply"] = response.content

    print("\n===== FINAL EMAIL =====")
    print(state["final_reply"])

    return state