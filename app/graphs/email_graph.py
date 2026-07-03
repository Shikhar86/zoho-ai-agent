from langgraph.graph import StateGraph, END

from app.models.state import EmailState

from app.agents.analyzer import analyze_email
from app.agents.planner import create_plan
from app.agents.memory import retrieve_memory
from app.agents.company import retrieve_company_context
from app.agents.search import search_internet
from app.agents.writer import write_reply
from app.agents.reviewer import review_reply

workflow = StateGraph(EmailState)

workflow.add_node("analyzer", analyze_email)
workflow.add_node("planner", create_plan)
workflow.add_node("memory", retrieve_memory)
workflow.add_node("company", retrieve_company_context)
workflow.add_node("search", search_internet)
workflow.add_node("writer", write_reply)
workflow.add_node("reviewer", review_reply)

workflow.set_entry_point("analyzer")

workflow.add_edge("analyzer", "planner")
workflow.add_edge("planner", "memory")
workflow.add_edge("memory", "company")
workflow.add_edge("company", "search")
workflow.add_edge("search", "writer")
workflow.add_edge("writer", "reviewer")
workflow.add_edge("reviewer", END)

graph = workflow.compile()