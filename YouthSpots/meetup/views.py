from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from meetup.models import MeetupData, MeetupUserData
import time
from django.urls import reverse




# Create your views here.
def meetup(request):
    return render(request, "meetup.html")
def my_meetup(request):
    return render(request, "meetup_created.html")
def meetup_edit(request):
    return render(request, "meetup_edit.html")

def meetup_data_create(request):
    if request.method == 'POST':
        name_meetup = request.POST.get('name_meetup')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')
        description = request.POST.get('description')
        #type_meetup = request.POST.get('type_meetup')
        #visibility = request.POST.get('visibility')
        if time_start >= time_end:
                  return HttpResponseBadRequest(render(request, 'meetup.html'))
                        
                  
              # Create a MeetupData instance
        meetup_data = MeetupData.objects.create(
            name_meetup=name_meetup,
            time_start=time_start,
            time_end=time_end,
            description=description,
           # type_meetup=type_meetup,
            #visibility=visibility
        )

       

    
    
      # Assuming 'meetup' is the name of your meetup URL pattern
        

    # Render a form for creating a meetup
    return render(request, 'meetup.html')
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
        meetup = MeetupData.objects.get(id=meetup_id)
        
        # Delete the meetup object from the database
        meetup.delete()

        # Optionally, you can return a success message or perform other actions
        return render(request, 'meetup.html')
    
    except MeetupData.DoesNotExist:
        return "Meetup with specified ID does not exist."
    
    except Exception as e:
        # Handle any other exceptions that may occur
        return f"An error occurred: {str(e)}"

#def meetup(request):
 #   type_mt = MeetupData.type_mt  # Retrieve type_mt from the MeetupData model
 #   return render(request, "meetup.html", {'type_mt': type_mt})