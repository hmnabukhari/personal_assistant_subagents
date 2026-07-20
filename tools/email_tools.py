from langchain_core.tools import tool


@tool
def send_email(recipient: str, subject: str, message: str) -> str:
    """Send an email."""

    return f"""
Email Sent Successfully

To: {recipient}
Subject: {subject}
Message:
{message}
"""