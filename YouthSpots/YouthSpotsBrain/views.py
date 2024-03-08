from django.http import JsonResponse
from django.shortcuts import render, redirect
from YouthSpotsBrain.models import EVCharcinglocation, UserAuth
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from geopy.distance import geodesic
import re
# Create your views here.
def home(request):
    if request.user.is_authenticated == False:
        return redirect("login")
    return render(request, "home.html")

def maps(request):
    stations = list(EVCharcinglocation.objects.values('latitude', 'longitude')[:100])
    # print(stations[:2])
    context = {'stations':stations}
    return render(request, "maps.html", context)

def nearest_station(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = latitude, longitude
    station_distances = {}
    for station in EVCharcinglocation.objects.all()[:100]:
        station_location = station.latitude, station.longitude
        
        distance = geodesic(user_location, station_location).km
        station_location[distance] = station_location
    min_distances = min(station_distances)
    station_coords = station_distances(min_distances)
    return JsonResponse({
        'coordinates': station_coords,
        'distance': min_distances
    })

def login(request):
    if request.method == "POST":
        if request.POST["username"] != "" or request.POST["password"] != "":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect("home")
            else:
                if UserAuth.objects.filter(username=username).exists():
                    user = UserAuth.objects.get(username=username)
                    if user.check_password(password):
                        return render(request, "home.html")
                    else:
                        return render(request, "login.html", {"error": "Invalid password"})
                else:
                    return render(request, "login.html", {"error": "Invalid username"})

        else:
            return render(request, "login.html", { "error": "Missing username or password"})
            
     

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        errors = []
        if request.POST["username"] == "":
            errors.append("Username is required")
        if request.POST["email"] == "":
            errors.append("Email is required")
        if request.POST["password"] != request.POST["password_confirm"]:
            errors.append("Passwords do not match")
        if len(request.POST["password"]) < 8:
            errors.append("Passwords must atleast be 8 characters long")
        if re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$", request.POST["password"]):
            errors.append("Password must contain atleast one uppercase letter, one lowercase letter and one number")
        if UserAuth.objects.filter(username=request.POST["username"]).exists():
            errors.append("Username already exists")
        if UserAuth.objects.filter(email=request.POST["email"]).exists():
            errors.append("Email already exists")
        if errors:
            return render(request, "signup.html", {"errors": errors})
        else:
            user = UserAuth.objects.create_user(
                request.POST["username"],
                request.POST["email"],
                request.POST["password"]
            )
            user.save()
            return redirect("login")
    return render(request, "signup.html")

def logout(request):
    django_logout(request)
    return redirect("login")

