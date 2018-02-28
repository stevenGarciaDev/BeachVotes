from django.conf.urls import url
from poll import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
