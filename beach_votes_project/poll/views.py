from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from poll.models import *
from poll.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'poll/index.html', {})

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', {})

@login_required
def create_poll(request):
    categories = Category.objects.all()

    context_dict = { 'categories' : categories}
    context_dict['invalid_input'] = False

    if request.method == 'POST':

        # use end_date field and instantiate a datetime object
        # end_date = request.POST.get('end_date')
        # end_date = end_date.split('-')
        #
        # year = int( end_date[0] )
        # month = int( end_date[1] )
        # day = int( end_date[2] )
        #
        # end_date_object = datetime.date(year, month, day)
        # title_question = request.POST.get('title_question')

        poll_form = PollForm()
        poll_form.title_question = request.POST.get('title_question')
        poll_form.end_date = request.POST.get('end_date')

        #print("the end date is {0} and the title is {1}".format( end_date_object, title_question))

        if poll_form.is_valid():

            poll = poll_form.save()

            # link the new poll with the corresponding Category table record
            selected_category = request.POST.get('category')
            category = Category.objects.get(group_name = selected_category)
            poll.category = category

            # link the new poll with the user that created it
            print("user id is {0}".format(request.user.id))

            User.objects.get( id = request.user.id )
            poll.poll_creator = user

            poll.save()

            print("successful")
            return render(request, 'poll/show_polls.html', {})
        else:
            context_dict['error_message'] = "Invalid input"
            print("invalid input, not valid form")

            print("here are the errors")
            print (poll_form.errors)
            print("here are the non field errors")
            print(poll_form.non_field_errors)
            return render(request, 'poll/create_poll.html', context_dict)

    else:
        # 'GET' request
        return render(request, 'poll/create_poll.html', context_dict)

@login_required
def my_profile(request):
    return render(request, 'poll/my_profile.html', {})

@login_required
def show_polls(request):
    return render(request, 'poll/show_polls.html', {})

@login_required
def view_poll(request):
    return render(request, 'poll/view_poll.html', {})

def login_user(request):
    context_dict = { 'invalid_input' : False }

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:

            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect(reverse('index'))
                return render(request, 'poll/show_polls.html', context_dict)
            else:
                context_dict['invalid_input'] = True
                return render(request, 'poll/login.html', context_dict)

        else:
            context_dict['invalid_input'] = True
            context_dict['error_message'] = "Invalid login details"
            return render(request, 'poll/login.html', context_dict)

    else:
        # 'GET' request
        return render(request, 'poll/login.html', {})

def sign_up(request):
    invalid_input = False

    if request.method == 'POST':

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

            return render(request, 'poll/show_polls.html', context = {})
        else:
            invalid_input = True
            error_message = "Invalid Input: Please fill in all fields"

            return render(request, 'poll/sign_up.html',
                context = {
                    'invalid_input': invalid_input,
                    'error_message': error_message})

    # in case of GET request
    return render(request, 'poll/sign_up.html', {})

def reset_password(request):
    return render(request, 'poll/reset_password.html', {})

def restricted_page(request):
    return render(request, 'poll/restricted_page.html', {})

# -----------------
# Helper methods
# -----------------
