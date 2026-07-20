from langchain_core.tools import tool


@tool
def create_calendar_event(title: str, date: str, time: str) -> str:
    """
    Create a calendar event.
    """

    return (
        f"Calendar event created:\n"
        f"Title: {title}\n"
        f"Date: {date}\n"
        f"Time: {time}"
    )