from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from poll.models import *
from poll.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
import datetime

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'poll/index.html', {})

#Combines a template with HttpResponse and returns rendered text via web
def index(request):
    return render(request, 'poll/index.html', {})

def successful_login(request):
    return render(request, 'poll/successful_login.html', {})

@login_required
def create_poll(request):
    categories = Category.objects.all()

    context_dict = { 'categories' : categories}
    context_dict['invalid_input'] = False

    if request.method == 'POST':

        try:
            poll = Poll()
            poll.title_question = request.POST.get('title_question')

            # use end_date field and instantiate a datetime object
            end_date = request.POST.get('end_date')
            end_date = end_date.split('-')

            year = int( end_date[0] )
            month = int( end_date[1] )
            day = int( end_date[2] )

            end_date_object = datetime.date(year, month, day)
            poll.end_date = end_date_object

            # link the new poll with the corresponding Category table record
            selected_category = request.POST.get('category')
            category = Category.objects.get(group_name = selected_category)
            poll.category = category

            # associate the poll with the user that created it
            user = User.objects.get( id = request.user.id )
            poll.poll_creator = user
            poll.save()

            # add choices
            # must construct a PollAnswerChoice
            # then link with Poll

            # should return an array
            answers = request.POST.getlist('answer')
            valid_answers = 0

            for answer in answers:

                # ensure value is not ""
                if not answer:
                    continue

                answer_choice = PollAnswerChoice(answer = answer)
                answer_choice.poll = poll
                answer_choice.save()

            context_dict['polls'] = Poll.objects.all()
            return render(request, 'poll/show_polls.html', context_dict)
        except:
            context_dict['error_message'] = "Invalid input"
            print("invalid input, not valid form")

            return render(request, 'poll/create_poll.html', context_dict)

    else:
        # 'GET' request
        return render(request, 'poll/create_poll.html', context_dict)

@login_required
def my_profile(request):
    return render(request, 'poll/my_profile.html', {})

@login_required
def show_polls(request):
    categories = Category.objects.all()
    polls = Poll.objects.order_by('-start_date')[:7]

    context_dict = { 'categories' : categories }
    context_dict['polls'] = polls
    return render(request, 'poll/show_polls.html', context_dict)

@login_required
def view_poll(request, poll_id, user_id):
    poll = Poll.objects.get(id = poll_id)
    user = User.objects.get(id = user_id)

    if poll.end_date < datetime.date.today() + datetime.timedelta(days=1):
        print("date has passed")
        vote_results = Vote.objects.filter(poll = poll)
        final_results = retrive_poll_results(poll)

        return render(request, 'poll/view_poll.html',
            context = {'poll': poll,
                       'poll_has_closed' : True,
                       'final_results' : final_results,
                       'vote_responses' : vote_results})

    try:
        # when user has already voted

        users_vote = Vote.objects.filter(poll = poll, user = user)
        print("user has voted")
        print(users_vote)

        if not users_vote:
            raise Exception("Vote not found")

        # retrieve results and send to webpage
        vote_results = Vote.objects.filter(poll = poll)
        final_results = retrive_poll_results(poll)

        return render(request, 'poll/view_poll.html',
            context = {'poll': poll,
                       'poll_has_closed' : True,
                       'final_results' : final_results,
                       'vote_responses' : vote_results })

    except Exception as exception:
        # when user has not voted

        answer_choices = PollAnswerChoice.objects.filter(poll = poll)
        print( str(exception) )

        return render(request, 'poll/view_poll.html',
            context = {'poll' : poll,
                       'poll_has_closed': False,
                       'answer_choices' : answer_choices })

@login_required
def view_category(request, category):
    context_dict = { 'polls' : Poll.objects.filter(category = category) }
    context_dict['category_name'] = Category.objects.get(id = category)
    return render(request, 'poll/view_category.html', context_dict)

@login_required
def view_all_polls(request):
    context_dict = { 'polls' : Poll.objects.all() }
    return render(request, 'poll/view_all_polls.html', context_dict)

@login_required
def vote_poll(request, user_id, poll_id):

    # post request
    if request.method == "POST":

        # instantiate a Vote object
        recent_vote = Vote()

        # connect it with the user and the corresponding poll
        current_poll = Poll.objects.get(id = poll_id)

        recent_vote.user = User.objects.get(id = user_id)
        recent_vote.poll = current_poll

        user_selected_choice = request.POST.get('vote_choice')
        answer_choice = PollAnswerChoice.objects.get(answer = user_selected_choice, poll = current_poll)
        recent_vote.vote_choice = answer_choice

        recent_vote.comment = request.POST.get('comment')

        recent_vote.save()

    return render(request, "poll/successful_vote.html", context =
        {'poll_id' : poll_id,
         'user_id' : user_id })

@login_required
def successful_vote(request, poll_id, user_id):
    return render(request, "poll/successful_vote.html", context =
        {'poll_id' : poll_id,
         'user_id' : user_id })

def login_user(request):
    context_dict = { 'invalid_input' : False }

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user is not None:

            if user.is_active:
                login(request, user)
                context_dict['polls'] = Poll.objects.all()
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

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)

            context_dict = { 'polls' : Poll.objects.all() }
            return render(request, 'poll/show_polls.html',  context_dict)
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

def retrive_poll_results(poll):
    # retrieve all possible choices
    answer_choices = PollAnswerChoice.objects.filter(poll = poll)

    # retrieve count for corresponding choice
    final_results = []
    for choice in answer_choices:
        total_count = Vote.objects.filter(poll = poll, vote_choice = choice.answer).count()
        final_results.append( [choice.answer, total_count] )

    # selection sort,
    i = 0
    while i < len(final_results):
        # find min
        # swap with i
        index_min_value = i

        n = i
        while n < len(final_results):
            min_result = final_results[ index_min_value ]
            current_result = final_results[n]

            if min_result[1] < current_result[1]:
                index_min_value = n

            n += 1

        # swap
        temp = final_results[i]
        final_results[i] = final_results[ index_min_value ]
        final_results[ index_min_value ] = final_results[i]

        # join data
        final_results[i] = "{answer_choice} - ({total_count})".format(
            answer_choice = final_results[i][0],
            total_count = final_results[i][1] )

        i += 1

    return final_results
