from django.urls import path
from . import views
# from YouthSpotsBrain import views
urlpatterns = [
    path("meetup_select/", views.select_meetup, name="select_meetup"),
    path('edit_meetup_details/', views.edit_meetup_details, name='edit_meetup_details'),
    path('my_meetups/', views.my_meetups, name='my_meetups'),
    path('meetup_public/', views.public_meetups, name='public_meetups'),
    path("meetup/", views.meetup, name="meetup"),
    # path('api/pin/<int:pin_id>/', views.get_pin, name='get_pin'),
    # path("create_meetup/", views.meetup_data_create, name="create_meetup"),
]

    