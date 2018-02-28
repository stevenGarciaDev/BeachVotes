from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    group_name = models.CharField(max_length = 30, unique = True, null = False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.group_name

class Poll(models.Model):
    category = models.ForeignKey(Category)
    title_question = models.CharField(max_length = 128, unique = True, null = False)
    start_date = models.DateTimeField( auto_now = False, auto_now_add = True, null = False)
    end_date =  models.DateTimeField

    def __str__(self):
        return self.title_question

class User(models.Model):
    username = models.CharField(max_length = 50, unique = True, null = False)
    email = models.EmailField(null = False)

    def __str__(self):
        return self.username

class Vote(models.Model):
    user = models.ForeignKey(User)
    vote_choice = models.CharField(max_length = 50, unique = False, null = False)
    comment = models.CharField(max_length = 144, unique = False, null = False)
    date_of_vote = models.DateTimeField( auto_now = False, auto_now_add = False, null = False )

    def __str__(self):
        return "The vote of : " + self.vote_choice + " was submitted by user:  " + self.user.username
