from django.urls import path
from . import views

urlpatterns = [
    path("", views.maps, name="map"),
    path("getPins/", views.getPins),
    path("savePin/", views.savePin),
    path('savePin/<int:pin_id>/', views.savePin, name='deletePin'),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("pins", views.pins, name="pins"),
    # path("meetups/", views.meetups, name="meetups"),
    # path("pins/", views.pins, name="pins"),
    # path("profile/", views.profile, name="profile"),
    path("profile-edit/", views.profile, name="profile-edit"),
    # path("settings/", views.settings, name="settings"),
    path("testpage/", views.home, name="test"),
]