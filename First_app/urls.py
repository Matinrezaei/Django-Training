from django.urls import path
from django.urls import include, re_path
from First_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^$', views.help, name='help'),
    re_path(r'^$', views.users, name='user'),
]