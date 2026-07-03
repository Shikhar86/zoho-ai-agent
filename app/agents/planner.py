def create_plan(state):

    print("PLANNER EXECUTED")

    plan = {
    "memory": state["requires_memory"],
    "company_context": True,
    "internet_search": state["requires_search"],
    "generate_reply": True,
    "review_reply": True,
    "human_review": state["requires_human"]
}

    state["plan"] = plan

    print("\n===== EXECUTION PLAN =====")
    print(plan)
    return state