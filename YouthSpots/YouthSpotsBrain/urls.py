from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.maps),
    path('get-nearest-station/', views.nearest_station)
]