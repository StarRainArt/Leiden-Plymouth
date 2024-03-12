from django.urls import path
from . import views

urlpatterns = [
    path("meetup_edit/", views.meetup_edit, name="meetup"),
    path("My_meetups/", views.my_meetup, name="meetup"),
    path("meetup/", views.meetup, name="meetup"),
    path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]

    