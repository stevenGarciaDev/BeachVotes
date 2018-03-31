from django.conf.urls import url
from poll import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^show_polls', views.show_polls, name='show_polls')
]
