from django.urls import path
from . import views

urlpatterns = [
    path("", views.maps, name="map"),
    path("getPins/", views.getPins),
    path("savePin/", views.savePin),
    path('savePin/<int:pin_id>/', views.savePin, name='deletePin'),
    path('pins/<int:pin_id>/', views.showMeetup, name='showMeetup'),
    path("pins", views.pins, name="pins"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"), 
    path("view_profile/", views.view_profile, name="view_profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    # path("meetups/", views.meetups, name="meetups"),
    path("settings/", views.settings, name="settings"),
    path("testpage/", views.home, name="test"),
    path("change_password/", views.change_password, name="changepassword"),
]