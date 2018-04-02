from django.shortcuts import render
from django.http import HttpResponse
from poll.models import *
from poll.forms import *

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        user_profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            # this hashes the password, encrypting it
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit = False)
            # here we link the models together as to form the
            # Foreign Key relationship between User and UserProfile
            user_profile.user = user

            registered = True

    # in case of GET request
    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    return render(request, 'poll/index.html',
        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
            'registered': registered})

def create_poll(request):
    return render(request, 'poll/create_poll.html', {})

def my_profile(request):
    return render(request, 'poll/my_profile.html', {})

def show_polls(request):
    return render(request, 'poll/show_polls.html', {})

def view_poll(request):
    return render(request, 'poll/view_poll.html', {})

def login(request):
    return render(request, 'poll/login.html', {})

def sign_up(request):
    return render(request, 'poll/sign_up.html', {})
