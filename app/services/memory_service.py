def get_memory_context(email_body):

    email = email_body.lower()

    if "quotation" in email:

        return """
Last conversation:

The customer requested a quotation for 200 software licenses.

Sales promised to send the quotation by Friday.
"""

    elif "meeting" in email:

        return """
Last meeting:

Meeting scheduled for Tuesday 3 PM.

Agenda:
- Product Demo
- Pricing
- Integration Timeline
"""

    return "No previous conversation found."