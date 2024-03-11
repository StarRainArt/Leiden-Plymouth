from django.urls import path
from . import views

urlpatterns = [
    path("", views.maps, name="map"),
    path("testpage/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path('get-nearest-station/', views.nearest_station)
]