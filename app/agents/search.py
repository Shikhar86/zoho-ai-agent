from app.services.search_service import get_internet_context


def search_internet(state):

    print("SEARCH AGENT EXECUTED")

    if not state["plan"]["internet_search"]:
        print("No internet search required.")

        state["internet_context"] = ""

        return state

    state["internet_context"] = get_internet_context(
        state["email_body"]
    )

    print("\n===== INTERNET CONTEXT =====")
    print(state["internet_context"])

    return state