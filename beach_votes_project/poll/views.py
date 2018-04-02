from django.shortcuts import render
from django.http import HttpResponse
from poll.models import *

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', context=None)

def create_poll(request):
    return render(request, 'poll/create_poll.html', {})

def my_profile(request):
    return render(request, 'poll/my_profile.html', {})

def show_polls(request):
    return render(request, 'poll/show_polls.html', {})

def view_poll(request):
    return render(request, 'poll/view_poll.html', {})
