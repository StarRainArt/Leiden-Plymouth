from django.urls import path
from . import views

urlpatterns = [
    path("", views.maps, name="map"),
    # path("meetups/", views.meetups, name="meetups"),
    # path("pins/", views.pins, name="pins"),
    # path("profile/", views.profile, name="profile"),
    path("profile-edit/", views.profile, name="profile-edit"),
    # path("settings/", views.settings, name="settings"),
    path('get-nearest-station/', views.nearest_station),
    path("testpage/", views.home, name="test"),
]