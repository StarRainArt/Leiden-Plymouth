from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from meetup.models import Meetups
from YouthSpotsBrain.models import Profile
from django.contrib.auth.decorators import login_required




# Create your views here.
def meetup(request):
    return render(request, "meetup.html")
def public_meetups(request):
    meetups = Meetups.objects.filter(visibility="Public" ) # and distance thing 101
    return render(request, 'meetup_public.html', {'meetups': meetups})
def my_meetups(request):
    profile = Profile.objects.get(user=request.user)
    User_id = Meetups.objects.get(owner=request.owner)
    meetups = Meetups.objects.filter(profile.id ==  User_id ) # filter(owner=id)Assuming Meetup is your model for storing meetup data
    return render(request, 'my_meetup.html', {'meetups': meetups})
def meetup_edit(request):
    return render(request, "meetup_edit.html")

@login_required
def meetup_data_create(request):
    if request.method == 'POST':
        # Extract form data
        name_meetup = request.POST.get('name_meetup')
        location = request.POST.get('location')
        visibility = request.POST.get('visibility')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')

        # Validate form data
        if None in [name_meetup, location, visibility, time_start, time_end, description]:
            return HttpResponseBadRequest(render(request, 'meetup.html'))

        # Create a new Meetups instance and save it to the database
        try:
            profile = Profile.objects.get(user=request.user)
            meetup = Meetups.objects.create(
                name_meetup=name_meetup,
                location=location,
                visibility=visibility,
                time_start=time_start,
                time_end=time_end,
                description=description,
                owner=profile
            )
            return HttpResponseRedirect('/')
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return HttpResponseBadRequest(render(request, 'meetup.html'))

    return render(request, 'meetup.html')

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

