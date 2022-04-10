from lib.email import email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
# from lib.stringtools import get_random_string
from .event import post_event


def register_new_user(name: str, password: str, email: str):
    # create an entry in database
    user = create_user(name,password,email)

    post_event('user_registered', user)


def forgotten_password(email:str):
    #retrieve user
    user = find_user(email)
    user_reset_code = get_random_string(16)

    post_event('user_password_forgottern')


