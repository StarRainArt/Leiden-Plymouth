from django.http import JsonResponse
from django.shortcuts import render
from YouthSpotsBrain.models import meetup_data, meetup_userdata
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


def Meetup_data(request):
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup') # don't forget to fix str stander if issue with int()
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        discription = request.POST.get('discription')
        #type_meetup = request.POST.get('type_meetup')
        visiablitie = request.POST.get('visiablitie')
        #if check 
        meetup_data.time_start = time_start,
        meetup_data.time_end = time_end,
        meetup_data.name_meetup = name_meetup,
        meetup_data.discription = discription,
        #meetup_data.type_meetup = type_meetup,
        meetup_data.visiablitie = visiablitie,
        
        # Process the username data as needed
    # Render your template or return an HTTP response