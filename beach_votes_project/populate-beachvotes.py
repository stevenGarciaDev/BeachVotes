import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'beach_votes_project.settings')

import django
django.setup()

from poll.models import Category

def populate():

    categories = [
        'Sports',
        'Science',
        'Entertainment',
        'Politics',
        'Relationships',
        'Food',
        'Other']

    i = 0
    while i < len(categories):
        add_category(categories[i])
        i += 1

def add_category(name):
    new_category = Category.objects.get_or_create(group_name = name)
    return new_category[0]

# start execution
if __name__ == '__main__':
    print("Starting BeachVotes population script")
    populate()
