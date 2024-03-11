from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("map/", views.maps),
    path("getPins/", views.getPins),
    path("savePin/", views.savePin),
    path('savePin/<int:pin_id>/', views.savePin, name='deletePin'),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("getPins/", views.getPins),
]