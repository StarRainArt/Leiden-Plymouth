from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import Meetups
from YouthSpotsBrain.models import Profile
from django import forms
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from .forms import MeetupsForm


# Create your views here.
def public_meetups(request):
    meetups = Meetups.objects.filter(visibility="Public" ) # and distance thing 101
    return render(request, 'meetup_public.html', {'meetups': meetups})

@login_required
# def my_meetups(request):
#     # Get the current user's profile
#     profile = Profile.objects.get(user=request.user)
    
#     # Filter meetups by the current user's profile
#     meetups = Meetups.objects.filter(owner=profile)
    
#     # Render the template with the meetups
#     return render(request, 'my_meetup.html', {'meetups': meetups})
def my_meetups(request):
    profile = Profile.objects.get(user=request.user)
    # User_id = Meetups.objects.get(owner=request.owner)
    # meetups = Meetups.objects.filter(profile.id ==  User_id ) 
    return render(request, 'my_meetup.html')

def meetup_edit(request):
    return render(request, "meetup_edit.html")

# class MeetupForm(forms.ModelForm):
#     class Meta:
#         model = Meetups
#         fields = ['name_meetup', 'location', 'visibility', 'time_start', 'time_end', 'description']

# def meetup_data_create(request):
#     if request.method == 'POST':
#         form = MeetupForm(request.POST)
#         if form.is_valid():
#             new_meetup = form.save(commit=False)
#             new_meetup.owner = Profile.objects.get(user=request.user)
#             new_meetup.save()
#             return redirect('meetup_list')  # or wherever you want to redirect after successful form submission
#     else:
#         form = MeetupForm()
#     return render(request, 'meetup.html', {'form': form})


# def meetup(request):
#     if request.method == 'POST':
#         form = MeetupsForm(request.POST)
#         if form.is_valid():
#             meetup = form.save(commit=False)
#             pin = form.cleaned_data.get('pin')
#             meetup.pin = pin
#             meetup.save()
#             return redirect('map')
#             # Redirect or render a template as needed
#     else:
#         form = MeetupsForm()
#     return render(request, 'meetup.html', {'form': form})

def meetup(request):
    pin_id = request.GET.get('pin_id')
    if pin_id:
        pin = get_object_or_404(Pins, id=pin_id)
        initial_data = {'pin': pin}
    else:
        initial_data = {}

    # Initialize form with initial data
    form = MeetupsForm(initial=initial_data)

    if request.method == 'POST':
        form = MeetupsForm(request.POST)
        if form.is_valid():
            new_meetup = Meetups.objects.create(
                 name_meetup=form.name_meetup,
                 location=form.location,
                 visibility=form.visibility,
                 time_start=form.time_start,
                 time_end=form.time_end,
                 description=form.description,
                 owner=form.profile)
            meetup = form.save()
            # owner = form.cleaned_data.get('profile')

            new_meetup = Meetups.objects.create(
                name_meetup=form.cleaned_data['name_meetup'],
                location=form.cleaned_data['location'],
                visibility=form.cleaned_data['visibility'],
                time_start=form.cleaned_data['time_start'],
                time_end=form.cleaned_data['time_end'],
                description=form.cleaned_data['description'],
                # owner=owner
            )
            return redirect('my_meetups')

    return render(request, 'meetup.html', {'form': form})


# @login_required
# def meetup_data_create(request):
#     if request.method == 'POST':
#         # Extract form data
#         name_meetup = request.POST.get('name_meetup')
#         location = request.POST.get('location')
#         visibility = request.POST.get('visibility')
#         time_start_str = request.POST.get('time_start')
#         time_end_str = request.POST.get('time_end')
#         description = request.POST.get('description')

#         # Validate form data
#         if None in [name_meetup, location, visibility, time_start_str, time_end_str, description]:
#             print("something")
#             return HttpResponseBadRequest(render(request, 'meetup.html'))

#         # Parse time data
#         try:
#             time_start = datetime.strptime(time_start_str, "%Y-%m-%d %H:%M:%S")
#             time_end = datetime.strptime(time_end_str, "%Y-%m-%d %H:%M:%S")
#         except ValueError:
#             print("Invalid time format")
#             return HttpResponseBadRequest(render(request, 'meetup.html'))

#         # Create a new Meetups instance and save it to the database
#         try:
#             profile = Profile.objects.get(user=request.user)
#             new_meetup = Meetups.objects.create(
#                 name_meetup=name_meetup,
#                 location=location,
#                 visibility=visibility,
#                 time_start=time_start,
#                 time_end=time_end,
#                 description=description,
#                 owner=profile
#             )
#             return HttpResponseRedirect('/')
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#             return HttpResponseBadRequest(render(request, 'meetup.html'))

    # return render(request, 'meetup.html')
#create_meetup_form.html is not const
def select_meetup(request):
    meetups = Meetups.objects.all()
    return render(request, 'select_meetup.html', {'meetups': meetups})

   

def edit_meetup_details(request, meetup_id):
    #meetup = Meetups.objects.get(id=meetup_id)
    meetup = Meetups.objects.get(pk=meetup_id)
    
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')
        #type_meetup = request.POST.get('type_meetup')
        visibility = request.POST.get('visibility')
        #latitude = lat
        #longitude = lng
        if None in [name_meetup, time_start, time_end, description, visibility]:
            return HttpResponseBadRequest("Required fields are missing.")
        try:# Update other fields as needed
            meetup.title=str(name_meetup),
            meetup.start_timestamp=int(time_start),
            meetup.end_timestamp=int(time_end),
            meetup.description=str(description),
            #meetup.longitude=lng,
            #meetup.latitude=lat,
            meetup.save()
        except ValueError as e:
            return HttpResponseBadRequest("Invalid data format.")
        return redirect('my_meetups')
#select_meetup.html is not const
    return render(request, 'my_meetups.html', {'meetup': meetup})
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

