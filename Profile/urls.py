from django.urls import include, re_path,path
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_view
from Profile.views import ProfileClass


app_name = 'Profile'
urlpatterns = [
    path('Profile',ProfileClass.as_view(), name = 'profile')
]
