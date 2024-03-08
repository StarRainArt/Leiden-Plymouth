from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.meetup, name="meetup"),
]