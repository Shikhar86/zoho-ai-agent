from app.services.llm import json_llm
import json


def analyze_email(state):

    print("ANALYZER EXECUTED")

    prompt = f"""
You are an intelligent email analysis agent.

Analyze the following email.

Subject:
{state["email_subject"]}

Body:
{state["email_body"]}

Thread:
{state.get("thread_context", "")}

Return ONLY valid JSON.

Format:

{{
    "intent": "",
    "urgency": "",
    "tone": "",
    "summary": "",
    "questions": [],
    "requires_memory": false,
    "requires_search": false,
    "requires_human": false
}}

Rules:

Intent should be one of:
- MEETING
- SALES
- SUPPORT
- INFORMATION
- COMPLAINT
- FOLLOW_UP
- OTHER

Urgency:
LOW
MEDIUM
HIGH

Tone:
Professional
Friendly
Angry
Neutral
Appreciative

requires_memory:
True if previous emails or company history are needed.

requires_search:
True if current internet information is needed.

requires_human:
True if legal, financial or sensitive decisions are involved.

Return ONLY JSON.
"""

    response = json_llm.invoke(prompt)

    print("\n===== RAW RESPONSE =====")
    print(response)

    print("\n===== CONTENT =====")
    print(response.content)

    analysis = json.loads(response.content)

    state["analysis"] = analysis

    state["intent"] = analysis["intent"]
    state["urgency"] = analysis["urgency"]
    state["tone"] = analysis["tone"]
    state["summary"] = analysis["summary"]

    state["questions"] = analysis["questions"]

    state["requires_memory"] = analysis["requires_memory"]
    state["requires_search"] = analysis["requires_search"]
    state["requires_human"] = analysis["requires_human"]

    return state