from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.maps),
    path('get-nearest-pin/', views.nearest_pin),
    path('api/save-marker', views.save_marker, name='save_marker'),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
]