from __future__ import unicode_literals

from django.db import models

#Creates model for - Categories: categorized by the following
#   Category type
class Category(models.Model):
    group_name = models.CharField(max_length = 30, unique = True, null = False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.group_name

#Creates model for - Polls: categorized by the following
#   Question -          This is the title of the poll as well as the question for the Poll
                            # This is a sequence of characters
#   Date of Creation -  The date stamping the creation of the Poll
#   End date -          Date in which the poll will/is closed
class Poll(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title_question = models.CharField(max_length = 128, unique = True, null = False)
    start_date = models.DateTimeField( auto_now = False, auto_now_add = True, null = False)
    end_date =  models.DateTimeField

    def __str__(self):
        return self.title_question

#Creates model for - User: categorized by the following
#   Username -  Unique identifier for a user, a sequence of characters that should be unique per user
#   Email    -  Unique identifier for proof of user authenticity
class User(models.Model):
    username = models.CharField(max_length = 50, unique = True, null = False)
    email = models.EmailField(null = False)

    def __str__(self):
        return self.username

#Creates model for - Votes: Categorized by the following
#   User    -   Links the specific user who has created the vote to prevent multiple cases of voting on the same Poll
#   Choice  -   The choice of the user given options provided by the polls
#   comment -   Comment by choice, left by the user should they choose
#   Date    -   Date stamping the date in which the user has cast the vote
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_choice = models.CharField(max_length = 50, unique = False, null = False)
    comment = models.CharField(max_length = 144, unique = False, null = False)
    date_of_vote = models.DateTimeField( auto_now = False, auto_now_add = False, null = False )

    def __str__(self):
        return "The vote of : " + self.vote_choice + " was submitted by user:  " + self.user.username
