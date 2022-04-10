from lib.email import email
from .event import subscribe

def handle_email_event(name, address, subject, body):
    send_email(f'{user.name} {user.address} sent email with subject {user.subject} with the content {user.body}')

def setup_email_event_handlers():
    subscribe("email", handle_email_event)

    