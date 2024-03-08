from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from YouthSpotsBrain.models import MeetupData, MeetupUserData
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


def meetup_data(request):
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')
        type_meetup = request.POST.get('type_meetup')
        location_meetup = request.POST.get('location_meetup')
        pins = request.POST.get('pins')
        visibility = request.POST.get('visibility')

        # Create a MeetupData instance
        meetup_data = MeetupData.objects.create(
            name_meetup=name_meetup,
            time_start=time_start,
            time_end=time_end,
            description=description,
            type_meetup=type_meetup,
            location_meetup=location_meetup,
            pins=pins,
            visibility=visibility
        )

        # For testing
        print(meetup_data.time_end)

        # Render a template or return a success message
        return HttpResponse("Meetup data saved successfully!")

    # Render a form for creating a meetup
    return render(request, 'create_meetup_form.html')
def meetup_data_test():
    # Simulated test data
    test_name_meetup = 'Test Meetup'
    test_time_start = '2024-03-08 10:00:00'
    test_time_end = '2024-03-08 12:00:00'
    test_description = 'This is a test meetup'
    test_type_meetup = 'FC'
    test_location_meetup = 12345
    test_pins = 10
    test_visibility = '+'

    # Create a MeetupData instance
    meetup_data = MeetupData.objects.create(
        name_meetup=test_name_meetup,
        time_start=test_time_start,
        time_end=test_time_end,
        description=test_description,
        type_meetup=test_type_meetup,
        location_meetup=test_location_meetup,
        pins=test_pins,
        visibility=test_visibility
    )

    # For testing
    print("name_meetup:", test_name_meetup)
    print("time_start:", test_time_start)
    print("time_end:", test_time_end)
    print("description:", test_description)
    print("type_meetup:", test_type_meetup)
    print("location_meetup:", test_location_meetup)
    print("pins:", test_pins)
    print("visibility:", test_visibility)

# Call the test function
meetup_data_test()