from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
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


def meetup_data_create(request):
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')
        type_meetup = request.POST.get('type_meetup')
        visibility = request.POST.get('visibility')

        # Create a MeetupData instance
        meetup_data = MeetupData.objects.create(
            name_meetup=name_meetup,
            time_start=time_start,
            time_end=time_end,
            description=description,
            type_meetup=type_meetup,
            visibility=visibility
        )

       

        # Render a template or return a success message
        return HttpResponse("Meetup data saved successfully!")

    # Render a form for creating a meetup
    return render(request, 'create_meetup_form.html')
#create_meetup_form.html is not const
def select_meetup(request):
    meetups = MeetupData.objects.all()
    return render(request, 'select_meetup.html', {'meetups': meetups})
#select_meetup.html is not const
def edit_meetup(request):
    if request.method == 'POST':
        meetup_id = request.POST.get('meetup_id')
        return redirect('edit_meetup', meetup_id=meetup_id)
#edit_meetup.html is not const    
def edit_meetup_details(request, meetup_id):
    meetup = MeetupData.objects.get(id=meetup_id)
    if request.method == 'POST':
        # Handle form submission to update the meetup details
        # This part depends on how your form is structured
        # For simplicity, let's assume the form is POSTed to this view
        # and we directly update the meetup instance
        meetup.name_meetup = request.POST.get('name_meetup')
        meetup.time_start = request.POST.get('time_start')
        meetup.time_end = request.POST.get('time_end')
        meetup.type_meetup = request.POST.get('type_meetup')
        meetup.visibility = request.POST.get('visibility')
        meetup.description = request.POST.get('description')
        # Update other fields as needed
        meetup.save()
        return redirect('select_meetup')
#select_meetup.html is not const
    return render(request, 'edit_meetup.html', {'meetup': meetup})
#edit_meetup.html is not const
#don't forget to add a something to remind people
from YouthSpotsBrain.models import MeetupData

def delete_meetup(meetup_id):
    try:
        # Retrieve the meetup object from the database based on the meetup_id
        meetup = MeetupData.objects.get(id=meetup_id)
        
        # Delete the meetup object from the database
        meetup.delete()

        # Optionally, you can return a success message or perform other actions
        return "Meetup deleted successfully."
    
    except MeetupData.DoesNotExist:
        return "Meetup with specified ID does not exist."
    
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"An error occurred: {str(e)}"

