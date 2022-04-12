from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home') 
    # setting up routers and functions when we reach a specific url, home is the name of the function we deifned in views.py
]