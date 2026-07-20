from langchain.agents import create_agent

from utils.llm import llm
from tools.calendar_tools import create_calendar_event


calendar_agent = create_agent(
    model=llm,
    tools=[create_calendar_event],
    system_prompt="""
You are a Calendar Assistant.

Your ONLY responsibility is managing calendar events.

Whenever the user asks to schedule, create, update or delete an event,
always use the calendar tool.

Never answer from your own knowledge if a tool can perform the task.
"""
)