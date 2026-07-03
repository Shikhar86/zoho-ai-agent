from fastapi import FastAPI
from pydantic import BaseModel

from app.graphs.email_graph import graph

app = FastAPI()


class EmailRequest(BaseModel):
    email_subject: str
    email_body: str
    thread_context: str = ""


@app.get("/")
def home():
    return {
        "message": "Zoho AI Email Assistant API is running!"
    }


@app.post("/generate_reply")
def generate_reply(request: EmailRequest):

    state = {
        "email_subject": request.email_subject,
        "email_body": request.email_body,
        "thread_context": request.thread_context
    }

    result = graph.invoke(state)

    return {
        "analysis": result.get("analysis"),
        "plan": result.get("plan"),
        "final_reply": result.get("final_reply")
    }