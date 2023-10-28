import os


from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

FROM = os.getenv('FROM')


def send_message(to: str, body: str) -> None:
    _ = client.messages.create(
        from_=FROM,
        body=body,
        to=to
    )
