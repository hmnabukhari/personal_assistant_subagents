from langchain_core.tools import tool

from integrations.google_calendar import create_google_calendar_event


@tool
def create_calendar_event(title: str, date: str, time: str) -> str:
    """
    Create a calendar event.
    """

    return create_google_calendar_event(title, date, time)