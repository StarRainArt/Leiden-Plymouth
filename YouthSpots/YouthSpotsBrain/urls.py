from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view_profile/", views.view_profile, name="view_profile"),

]