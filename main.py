from app.graphs.email_graph import graph


state = {
    "email_subject": "AI News",
    "email_body": "What are the latest OpenAI announcements?",
    "thread_context": ""
}

result = graph.invoke(state)

print("\n========== ANALYSIS ==========")
print(result.get("analysis"))

print("\n========== EXECUTION PLAN ==========")
print(result.get("plan"))

print("\n========== FINAL EMAIL ==========\n")
print(result.get("final_reply"))