from app.services.company_service import get_company_context


def retrieve_company_context(state):

    print("COMPANY AGENT EXECUTED")

    if not state["plan"]["company_context"]:
        print("No company context required.")

        state["company_context"] = ""

        return state

    state["company_context"] = get_company_context(
        state["email_body"]
    )

    print("\n===== COMPANY CONTEXT =====")
    print(state["company_context"])

    return state