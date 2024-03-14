from django.urls import path
from . import views

urlpatterns = [
    path("meetup_edit/", views.meetup_edit, name="meetup_edit"),
    path('my_meetups/', views.my_meetups, name='my_meetups'),
    path('meetup_public/', views.public_meetups, name='public_meetups'),
    path("meetup/", views.meetup, name="meetup"),
    path('api/pin/<int:pin_id>/', views.get_pin, name='get_pin'),
    # path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]

    