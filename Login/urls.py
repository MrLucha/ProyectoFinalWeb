from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib import admin

from . import views
from django.contrib.auth import views as auth_views

#VISTAS
#from Login.views import Index

from Login.views import LoginClass
from Landing.views import LandingClass
from Profile.views import ProfileClass
#from Login.views import Landing
#URL QUE MANEJAN LOS PARAMETROS DASHBOARD
app_name = 'Login'

urlpatterns = [

    path('',LoginClass.as_view(), name = 'login'),
]
