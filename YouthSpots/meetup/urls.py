from django.urls import path
from . import views

urlpatterns = [
    path("meetup_select/<int:meetup_id>/", views.edit_meetup, name="select_meetup"),
    path('edit_meetup_details/<str:meetup_id>/', views.edit_meetup_details, name='edit_meetup_details'),
    path('my_meetups/', views.my_meetups, name='my_meetups'),
    path('meetup_public/', views.public_meetups, name='public_meetups'),
    path("meetup/", views.meetup, name="meetup"),
    path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]


    