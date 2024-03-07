from django.http import JsonResponse
from django.shortcuts import render
from YouthSpotsBrain.models import Meetups
from YouthSpotsBrain.models import Pins
from geopy.distance import geodesic
# Create your views here.
def home(request):
    return render(request, "home.html")

def maps(request):
    pins = list(Pins.objects.values('id', 'title', 'description', 'latitude', 'longitude', 'tags', 'created_timestamp')[:100])
    # print(pins[:2])
    context = {'pins':pins}
    return render(request, "maps.html", context)

def nearest_pin(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = latitude, longitude
    pin_distances = {}
    for pin in Pins.objects.all()[:100]:
        pin_location = pin.latitude, pin.longitude
        
        distance = geodesic(user_location, pin_location).km
        pin_location[distance] = pin_location
    min_distances = min(pin_distances)
    pin_coords = pin_distances(min_distances)
    return JsonResponse({
        'coordinates': pin_coords,
        'distance': min_distances
    })
