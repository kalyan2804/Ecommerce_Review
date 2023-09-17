from django.urls import path
from . import views
urlpatterns = [
    path('', views.generate, name='generate'),     #navigates the url to the home page describing function
    path('proceed', views.proceed, name='proceed'), #path for the form button submit
]