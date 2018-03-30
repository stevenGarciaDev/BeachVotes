from django.shortcuts import render
from django.http import HttpResponse

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', context=None)
