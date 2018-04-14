from django.contrib import admin
from poll.models import Category, User, UserProfile, Poll, PollAnswerChoice, Vote

# Register your models here.

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Poll)
admin.site.register(PollAnswerChoice)
admin.site.register(Vote)
