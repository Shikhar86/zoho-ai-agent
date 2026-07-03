def decide_route(state):

    route = state["route"]

    if route == "MEMORY":
        return "memory"

    if route == "SEARCH":
        return "search"

    return "writer"