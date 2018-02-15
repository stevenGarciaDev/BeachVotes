from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'my message'}

    return render(request, 'polling/index.html', context = context_dict)
