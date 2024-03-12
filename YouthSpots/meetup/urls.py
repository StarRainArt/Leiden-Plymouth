from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.meetup, name="meetup"),
    path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]

def create_meetup(request):
    views.meetup_data_create
    