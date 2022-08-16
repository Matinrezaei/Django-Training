from django.urls import path, include, re_path
from First_app import views


app_name = 'basic_app'

urlpatterns = [
   
    path('relative/', views.relative, name='relative'),
    path('register/', views.register, name='register'),
    path('other/', views.other, name='other'),
    path('user_login/', views.user_login, name='user_login'),
]