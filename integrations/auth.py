from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Permissions your assistant needs
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
]

BASE_DIR = Path(__file__).resolve().parent.parent

TOKEN_FILE = BASE_DIR / "token.json"
CREDENTIALS_FILE = BASE_DIR / "credentials.json"


from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send",
]

BASE_DIR = Path(__file__).resolve().parent.parent

TOKEN_FILE = BASE_DIR / "token.json"
CREDENTIALS_FILE = BASE_DIR / "credentials.json"


def authenticate_google():

    creds = None

    # Load saved credentials
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(
            str(TOKEN_FILE),
            SCOPES,
        )

    # If credentials are invalid
    if not creds or not creds.valid:

        # Refresh existing token
        if creds and creds.expired and creds.refresh_token:

            creds.refresh(Request())

        # Login again
        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE),
                SCOPES,
            )

            creds = flow.run_local_server(
                host="localhost",
                port=8080,
                open_browser=True,
            )

        # Save updated credentials
        TOKEN_FILE.write_text(
            creds.to_json()
        )

    return creds
    