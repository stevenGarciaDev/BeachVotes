from django.conf.urls import url
from forum import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^show', views.show, name='show'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
    url(r'^reset_password', views.reset_password, name='reset_password'),
]
