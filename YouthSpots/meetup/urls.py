from django.urls import path
from . import views

urlpatterns = [
    path("meetup/", views.meetup, name="meetup"),
]

def create_meetup(request):
    views.meetup_data_create
    