from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.meetup, name="meetup"),
]

def create_meetup():
    views.meetup_data_create