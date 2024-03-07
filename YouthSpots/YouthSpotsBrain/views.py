from django.http import JsonResponse
from django.shortcuts import render
from YouthSpotsBrain.models import EVCharcinglocation, UserAuth
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
    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        errors = []
        if request.POST.get("password") != request.POST.get("password_confirm"):
            errors.append("Passwords do not match")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password = request.POST.get("password_confirm")
        print(username, email, password)
    return render(request, "signup.html")

