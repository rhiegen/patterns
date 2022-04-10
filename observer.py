from api.user import register_new_user, forgotten_password
from api.plan import upgrade_plan
from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_event_handlers
from api.email_listerner import setup_email_event_handlers

setup_log_event_handlers()
setup_slack_event_handlers()
setup_email_event_handlers()


# register a new user
register_new_user('fulano', 'my_pass','myemail@gmail.com')

# send a password messagem
forgotten_password('myemail@gmail.com')

# upgrade the plan
upgrade_plan('myemail@gmail.com')