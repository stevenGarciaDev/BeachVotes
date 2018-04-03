from django.conf.urls import url
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_poll', views.create_poll, name='create_poll'),
    url(r'^my_profile', views.my_profile, name='my_profile'),
    url(r'^show_polls', views.show_polls, name='show_polls'),
    url(r'^view_poll', views.view_poll, name='view_poll'),
    url(r'^login', views.login, name='login'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^restricted', views.restricted, name = 'restricted')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
