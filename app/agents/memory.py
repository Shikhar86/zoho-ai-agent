from app.services.memory_service import get_memory_context


def retrieve_memory(state):

    print("MEMORY AGENT EXECUTED")

    if not state.get("plan", {}).get("memory", False):
        print("No memory required.")

        state["memory_context"] = ""

        return state

    state["memory_context"] = get_memory_context(
        state["email_body"]
    )

    print("\n===== MEMORY =====")
    print(state["memory_context"])

    return state
