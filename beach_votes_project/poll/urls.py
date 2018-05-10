from django.conf.urls import url
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^show_polls', views.show_polls, name='show_polls'),
    url(r'^(?P<poll_id>[0-9]+)$', views.view_poll, name='view_poll'),
    url(r'^category/(?P<category>[0-9]+)/$', views.view_category, name='view_category'),
    url(r'^login', views.login_user, name='login'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^reset_password', views.reset_password, name = 'reset_password'),
    url(r'^restricted_page', views.restricted_page, name = 'restricted_page'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^vote_poll/(?P<user_id>[0-9]+)/(?P<poll_id>[0-9]+)/$', views.vote_poll, name='vote_poll'),
    url(r'^successful_login', views.successful_login, name='successful_login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
