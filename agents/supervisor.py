from langchain.agents import create_agent

from utils.llm import llm
from agents.calendar_agent import calendar_agent
from agents.email_agent import email_agent
from langchain_core.tools import tool


@tool
def calendar_assistant(query: str) -> str:
    """Delegate calendar-related tasks to the Calendar Agent."""

    response = calendar_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    return response["messages"][-1].content


@tool
def email_assistant(query: str) -> str:
    """Delegate email-related tasks to the Email Agent."""

    response = email_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    return response["messages"][-1].content


supervisor = create_agent(
    model=llm,
    tools=[
        calendar_assistant,
        email_assistant,
    ],
    system_prompt="""
You are a Personal AI Assistant.

You NEVER perform tasks yourself.

If the user asks about:

• meetings
• appointments
• schedules
• calendar

use the Calendar Assistant.

If the user asks about:

• email
• send email
• compose email
• reply email

use the Email Assistant.

Always delegate to the appropriate assistant.
"""
)