from lib.slack import post_slack_message
from .event import subscribe

def handle_user_requested_event(user):
    post_slack_message("sales", f'{user.name} has registered with email {user.email}. Do not forget to spam this person.')

def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_requested_event)

    