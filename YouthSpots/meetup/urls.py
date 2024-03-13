from django.urls import path
from . import views

urlpatterns = [
    path("meetup_edit/", views.meetup_edit, name="edit_meetup"),
    path("meetup_edit/", views.edit_meetup_details, name="editing_meetup"),
    path('my_meetups/', views.my_meetups, name='my_meetups'),
    path('meetup_public/', views.public_meetups, name='public_meetups'),
    path("meetup/", views.meetup, name="meetup"),
    path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]


    