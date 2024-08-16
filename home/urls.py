__author__ = "Farhad Allian"

from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorised', views.AuthorisedView.as_view())
]