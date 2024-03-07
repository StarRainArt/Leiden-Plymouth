from django.http import JsonResponse
from django.shortcuts import render
from YouthSpotsBrain.models import EVCharcinglocation, UserAuth
from django.contrib.auth import authenticate
from geopy.distance import geodesic
# Create your views here.
def home(request):
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
            if UserAuth.objects.filter(username=username).exists():
                authenticate()
        else:
            return render(request, "login.html", { "error": "Missing username or password"})
     

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        errors = []
        if request.POST["password"] != request.POST["password_confirm"]:
            errors.append("Passwords do not match")
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
            return render(request, "login.html")
    return render(request, "signup.html")

