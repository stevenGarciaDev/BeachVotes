from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from poll.models import *
from poll.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def restricted(request):
    return HttpResponse("Logged in")

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', {})

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
    registered = False

    if request.method == 'POST':

        # user_form = UserForm()
        # user_form.username = request.POST.get('username')
        # user_form.email = request.POST.get('email')
        # user_form.input_password = request.POST.get('password')
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # this hashes the password, encrypting it
            user.set_password(user.password)
            user.save()

            user_profile = profile_form.save(commit = False)

            # link together models of user_profile and user together
            # Foreign Key relationship between User and UserProfile
            user_profile.user = user
            user_profile.save()

            registered = True

            print("successful")

    # in case of GET request
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'poll/sign_up.html',
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered})

def reset_password(request):
    return render(request, 'poll/reset_password.html', {})
