import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'beach_votes_project.settings')

import django
django.setup()

from poll.models import *

def populate():

    users = [

    ]

    user_profiles = [

    ]

    polls = [
        {'title_question': '',
         'end_date': },
        {'title_question': '',
         'end_date': },
        {'title_question': '',
         'end_date': },
        {'title_question': '',
         'end_date': }
    ]
