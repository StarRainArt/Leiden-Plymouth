from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("map/", views.maps),
<<<<<<< HEAD
=======
    path("getPins/", views.getPins),
    path("savePin/", views.savePin),
    path('get-nearest-pin/', views.nearest_pin),
>>>>>>> 96d644f38692747e7cf03a4329242c5130ad47c9
    path('api/save-marker', views.save_marker, name='save_marker'),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("getPins/", views.getPins),
]