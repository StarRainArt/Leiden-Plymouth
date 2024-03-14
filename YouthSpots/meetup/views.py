from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import Meetups
from YouthSpotsBrain.models import Profile, Pins
from django import forms
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render
from .forms import MeetupsForm, MeetupsForm_Edit
from django.urls import reverse


# Create your views here.
def public_meetups(request):
    meetups = Meetups.objects.filter(visibility="Public" ) # and distance thing 101
    return render(request, 'meetup_public.html', {'meetups': meetups})

@login_required
def my_meetups(request):
    # Get the current user's profile
    profile = Profile.objects.get(user=request.user)
    
    # Filter meetups by the current user's profile
    meetups = Meetups.objects.filter(owner=profile)
    
    # Render the template with the meetups
    return render(request, 'my_meetup.html', {'meetups': meetups})


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
            # meetup = form.save()

            new_meetup = Meetups.objects.create(
                name_meetup=form.cleaned_data['name_meetup'],
                location=form.cleaned_data['location'],
                visibility=form.cleaned_data['visibility'],
                time_start=form.cleaned_data['time_start'],
                time_end=form.cleaned_data['time_end'],
                description=form.cleaned_data['description'],
                owner=request.user.profile
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
    meetup_id=int(request.POST.get('meetup_id'))
    meetups = Meetups.objects.all()
    meetup_used=Meetups.objects.filter(id=meetup_id).first
    request.session['selected_meetup_id'] = meetup_id
    return  redirect( reverse('edit_meetup_details') ) #request,{'meetups': meetups},

   

def edit_meetup_details(request):
    #meetup = Meetups.objects.get(id=meetup_id)
    meetup_id = request.session.get('selected_meetup_id')
    meetup = Meetups.objects.get(id=meetup_id)
    form = MeetupsForm_Edit(request.POST,instance=meetup)
    
    if form.is_valid():
     meetup.name_meetup=form.cleaned_data['name_meetup'],
     meetup.location=form.cleaned_data['location'],
     meetup.visibility=form.cleaned_data['visibility'],
     meetup.time_start=form.cleaned_data['time_start'],
     meetup.time_end=form.cleaned_data['time_end'],
     meetup.description=form.cleaned_data['description'],
     meetup = form.save()
     return redirect('my_meetups')
    else:
         form = MeetupsForm_Edit(instance=meetup, initial={
            'location': meetup.location,
            'name_meetup': meetup.name_meetup,
            'description': meetup.description,
            'time_start': meetup.time_start,
            'time_end': meetup.time_end,
            #'invited': meetup.invited,
            #'tags': meetup.tags.all() if hasattr(meetup, 'tags') and hasattr(meetup.tags, 'all') else None,
            'pin': meetup.pin,
            #'visibility': meetup.visibility,
             })
# #select_meetup.html is not const
    return render(request, 'meetup_edit.html', {'form': form,'meetup': meetup})
# #edit_meetup.html is not const
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

