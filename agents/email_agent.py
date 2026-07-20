from langchain.agents import create_agent

from utils.llm import llm
from tools.email_tools import send_email


email_agent = create_agent(
    model=llm,
    tools=[send_email],
    system_prompt="""
You are an Email Assistant.

Your ONLY responsibility is sending emails.

Whenever the user asks to send, compose or email someone,
always use the email tool.

Never answer from your own knowledge if a tool can perform the task.
"""
)