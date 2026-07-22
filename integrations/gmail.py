import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from integrations.auth import authenticate_google


def send_email(to, subject, body):
    """
    Send an email using Gmail API.
    """

    creds = authenticate_google()

    service = build(
        "gmail",
        "v1",
        credentials=creds,
    )

    message = MIMEText(body)

    message["to"] = to
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    send_message = (
        service.users()
        .messages()
        .send(
            userId="me",
            body={"raw": raw_message},
        )
        .execute()
    )

    return send_message["id"]