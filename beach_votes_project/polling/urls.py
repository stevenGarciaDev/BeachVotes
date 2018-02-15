from django.conf.urls import url
from polling import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
