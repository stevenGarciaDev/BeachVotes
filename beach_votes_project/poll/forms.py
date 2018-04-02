from django import forms
from django.contrib.auth.models import User
from poll.models import Category, Poll, Vote, UserProfile

class CategoryForm(forms.ModelForm):
    group_name = forms.CharField(label = 'Category Name',
                                max_length = 50,
                                help_text = 'Please enter the category name')
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = Category
        fields = ('group_name'))

class PollForm(forms.ModelForm):
    title_question = forms.CharField(label = 'Title',
                                    max_length = 128,
                                    help_text = 'Please enter the poll title'))
    end_date = forms.DateField(label = 'Closing Date', required = True)
    start_date = forms.DateField(widget = forms.HiddenInput())

    class Meta:
        model = Poll
        fields = ('title_question', 'category')

class PollAnswerChoiceForm(forms.ModelForm):
    answer = forms.CharField(max_length = 50)

    class Meta:
        model = PollAnswerChoice
        fields = ('answer')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ()

class VoteForm(forms.ModelForm):
    comment = forms.CharField(label = 'Comment',
                                max_length = 144,
                              help_text = 'Please enter a comment')
    vote_choice = forms.CharField(max_length = 50)

    class Meta:
        model = Vote
        fields = ('vote_choice', 'comment')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
