from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile")
    path("map/", views.maps),
    path('get-nearest-station/', views.nearest_station)
]