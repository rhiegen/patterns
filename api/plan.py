from lib.email import email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
# from lib.stringtools import get_random_string


def upgrade_plan(email: str):
    
    #find user
    user = find_user(email)
    
    #upgrade plan
    user.plan = 'paid'

    #post a Slack message to sales department
    post_slack_message('sales',f'{user.name} has upgraded their plan')

    # send a thank you e-mail
    send_email(user.name, user.email, 'Thank you',
    f'Thanks for upgrading {user.name} you are gonna love it!. \nRegards, the Devnotes team.')

    #write a server log
    log(f'{user.name} has upgraded their plan.')

