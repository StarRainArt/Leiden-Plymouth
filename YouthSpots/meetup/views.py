from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
#from meetup.models import MeetupData
from YouthSpotsBrain.models import Profile, Meetups, Pins
import time, datetime
from django.urls import reverse




# Create your views here.
def meetup(request):
    return render(request, "meetup.html")
def public_meetups(request):
    meetups = Meetups.objects.filter(visibility="Public" ) # and distance thing 101
    return render(request, 'meetup_public.html', {'meetups': meetups})
def my_meetups(request):
    # Filter meetups based on the owner_id field
    #meetups = Meetups.objects.filter(owner_id=request.user.profile) #filter it to owner
    user_id = 1#request.user.id
    meetups =Meetups.objects.filter(owner_id=user_id)
    return render(request, 'My_meetup.html', {'meetups': meetups})
    
def meetup_edit(request):
    return render(request, "meetup_edit.html")

def meetup_data_create(request):
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')
        #type_meetup = request.POST.get('type_meetup')
        visibility = request.POST.get('visibility')
        if request.method == 'GET':
           lat = request.GET.get('lat')
           lng = request.GET.get('lng')
           title = request.GET.get('title')
         
        user_id = Profile.objects.values_list('id', flat=True).first()
        #profile = Profile.objects.get()
        profile = Profile.objects.get(id=user_id)
        
        #or time_start <= time.localtime
        if time_start >= time_end :
            return HttpResponseBadRequest(render(request, 'meetup.html'))
                        
                  
              # Create a MeetupData instance
        Meetup = Meetups.objects.create(
            title=name_meetup,
            start_timestamp=time_start,
            end_timestamp=time_end,
            description=description,
            owner_id=profile,
            longitude=lng,
            latitude=lat,
            
           # type_meetup=type_meetup,
            visibility=visibility
        )

       

    
    
      # Assuming 'meetup' is the name of your meetup URL pattern
        

    # Render a form for creating a meetup
    return render(request, 'maps.html')
#create_meetup_form.html is not const
def select_meetup(request):
    meetups = Meetups.objects.all()
    return render(request, 'select_meetup.html', {'meetups': meetups})

def edit_meetup(request):
    if request.method == 'POST':
        meetup_id = request.POST.get('meetup_id')
        return redirect('edit_meetup', meetup_id=meetup_id)
#edit_meetup.html is not const    

def edit_meetup_details(request, meetup_id):
    meetup = Meetups.objects.get(id=meetup_id)
    if request.method == 'POST':
        meetup.name_meetup = request.POST.get('name_meetup')
        meetup.time_start = request.POST.get('time_start')
        meetup.time_end = request.POST.get('time_end')
        #meetup.type_meetup = request.POST.get('type_meetup')
        #meetup.visibility = request.POST.get('visibility')
        meetup.description = request.POST.get('description')
        # Update other fields as needed
        meetup.save()
        return redirect('select_meetup')
#select_meetup.html is not const
    return render(request, 'edit_meetup.html', {'meetup': meetup})
#edit_meetup.html is not const
#don't forget to add a something to remind people


def delete_meetup(meetup_id, request):
    try:
        # Retrieve the meetup object from the database based on the meetup_id
        meetup = Meetups.objects.get(id=meetup_id)
        
        # Delete the meetup object from the database
        meetup.delete()

        # Optionally, you can return a success message or perform other actions
        return render(request, 'meetup.html')
    
    except Meetups.DoesNotExist:
        return "Meetup with specified ID does not exist."
    
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"An error occurred: {str(e)}"

