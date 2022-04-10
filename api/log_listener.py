from lib.log import log
from .event import subscribe

def handle_user_requested_event(user):
    log(f'User registered with email {user.email}')

def handle_user_password_forgotten_event(user):
    log(f'User with email {user.email} requested a password reset')

def setup_log_event_handlers():
    subscribe("user_registered", handle_user_requested_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)

    