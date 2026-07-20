def create_google_calendar_event(title: str, date: str, time: str) -> str:
    """
    Simulates creating an event in Google Calendar.
    Later this function will call the real Google Calendar API.
    """

    return (
        f"✅ Google Calendar Event Created\n\n"
        f"Title: {title}\n"
        f"Date: {date}\n"
        f"Time: {time}"
    )