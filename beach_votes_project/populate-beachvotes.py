import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'beach_votes_project.settings')

import django
django.setup()

from poll.models import Category

def populate():

    users = [
        'EricIsAwesome555',
        'RealName205',
        'Anonymous',
        'GeorgeTheMonkey',
        'BobBuilder',
        'SpongeSquare',
        'AAAH',
        'OrangeJuice'
    ]
    i = 0
    while i < len(users):
        add_user(users[i])
        i++

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

    Poll = [
        {"category":"Sports",
         "poll_creator":"RealName205",
         "title_question":"Should I go pro?",
         "start_date":"5/1/2018",
         "end_date":"6/1/2018"},
        {"category":"Science",
         "poll_creator":"BobBuilder",
         "title_question":"Is monkey man?",
         "start_date":"5/3/2018",
         "end_date":"6/5/2018"},
        {"category":"Relationships",
         "poll_creator":"AAAH",
         "title_question":"Should I marry?",
         "start_date":"5/5/2018",
         "end_date":"7/2/2018"},
        {"category":"Food",
         "poll_creator":"OrangeJuice",
         "title_question":"Oranges good?",
         "start_date":"5/1/2018",
         "end_date":"6/5/2018"}
    ]
    #i = 0
    #while i < len(Poll):
    #    add_poll()
    #    i += 1

    PollChoices = [
        {"poll":"Should I go pro?",
         "answer":"Yes!"},
        {"poll":"Should I go pro?",
         "answer":"No!"},
        {"poll":"Is monkey man?",
         "answer":"Yes!"},
        {"poll":"Is monkey man?",
         "answer":"No!"},
        {"poll":"Should I marry?",
         "answer":"Of Course!"},
        {"poll":"Should I marry?",
         "answer":"NOOOO!"},
        {"poll":"Oranges good?",
         "answer":"Obviously!"}
        {"poll":"Oranges good?",
         "answer":"NOPE!"}
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    vote_choice = models.CharField(max_length = 50, unique = False, null = False)
    comment = models.CharField(max_length = 144, unique = False, null = False)
    date_of_vote = models.DateField(null = False)
    Votes = [
        {"user":"Bobbuilder",
         "poll":"--------",
         "vote_choice":"Yes!",
         "comment":"",
         "date_of_vote":"5/6/2018"}
    ]

def add_category(name):
    new_category = Category.objects.get_or_create(group_name = name)
    return new_category[0]

def add_user(name):
    new_user = User.objects.get_or_create(name = name)

def add_poll(cat, creator, quest, start, end):
    p = Poll.objects.get_or_create(category = cat, poll_creator = creator)
    p.title_question = quest
    p.start_date = start
    p.end_date = end

# start execution
if __name__ == '__main__':
    print("Starting BeachVotes population script")
    populate()
