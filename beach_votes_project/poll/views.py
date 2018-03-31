from django.shortcuts import render
from django.http import HttpResponse

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', context=None)

def create_poll(request):
    return HttpResponse("create a poll")

def my_profile(request):
    return HttpResponse("my profile")

def show_polls(request):
    return HttpResponse("show polls")
