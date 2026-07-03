from typing import TypedDict

class EmailState(TypedDict, total=False):
    email_subject: str
    email_body: str
    thread_context: str

    analysis: dict

    intent: str
    urgency: str
    tone: str
    summary: str
    questions: list

    requires_memory: bool
    requires_search: bool
    requires_human: bool

    plan:dict
    
    memory_context: str
    company_context: str
    internet_context: str

    draft_reply: str
    final_reply: str