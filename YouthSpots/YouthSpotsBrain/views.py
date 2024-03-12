from django.http import JsonResponse, HttpResponse
from YouthSpotsBrain.models import Meetups, Profile, Pins, UserAuth, Tags
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from geopy.distance import geodesic
import json
import re
def home(request):
    if request.user.is_authenticated == False:
        return redirect("login")
    return render(request, "home.html")

def view_profile(request):
    if request.user.is_authenticated == False:
        return redirect("login")
    if request.method == "POST":
        if request.POST.get("action") == "tags":
            if request.POST.get("name") != None:
                profile = Profile.objects.get(user=request.user)
                if Tags.objects.filter(name=request.POST.get("name")).exists():
                    tag = Tags.objects.get(name=request.POST.get("name"))
                    profile.favorite_tags.add(tag)
                    profile.save()
                else:
                    tag = Tags(name=request.POST.get("name"))
                    tag.save()
                    profile.favorite_tags.add(Tags.objects.get(name=request.POST.get("name")))
                    profile.save()
            elif request.POST.get("action") == "bio":
                profile = Profile.objects.get(user=request.user)
                profile.biography = request.POST.get("biography")
                profile.save()
            elif request.POST.get("task") == "remove":
                print("test")
                profile = Profile.objects.get(user=request.user)
                tag = Tags.objects.get(name=request.POST.get("name"))
                profile.favorite_tags.remove(tag)
                profile.save()
    profile = Profile.objects.get(user=request.user)
    return render(request, "view_profile.html", {"biography": profile.biography, "favorite_tags": profile.favorite_tags.all()})

def edit_profile(request):
    return render(request, "edit_profile.html")

def maps(request):
    return render(request, "maps.html")

def getPins(request):
    return JsonResponse(list(Pins.objects.values('id', 'title', 'description', 'latitude', 'longitude', 'tags', 'created_timestamp')[:100]), safe=False)


def savePin(request, pin_id=None):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        # Check if a pin with the same latitude and longitude already exists
        existing_pin = Pins.objects.filter(latitude=lat, longitude=lng).first()
        if existing_pin:
            # Update the existing pin
            existing_pin.title = title
            existing_pin.description = description
            existing_pin.tags = tags
            existing_pin.save()
            return JsonResponse({'status': 'Updated'})
        else:
            # Create a new pin
            pin = Pins(title=title, description=description, latitude=lat, longitude=lng, tags=tags)
            pin.save()
            return JsonResponse({'status': 'Created'})
    elif request.method == 'DELETE':
        if pin_id is not None:
            try:
                pin = Pins.objects.get(pk=pin_id)
            except Pins.DoesNotExist:
                return JsonResponse({'status': 'Not Found'}, status=404)
            pin.delete()
            return JsonResponse({'status': 'Deleted'})
        else:
            return JsonResponse({'status': 'Bad Request: No pin id provided'}, status=400)
    else:
        return JsonResponse({'status': 'Method Not Allowed'}, status=405)

def showMeetup(request, pin_id=None):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tags = request.POST.get('tags')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        # Check if a pin with the same latitude and longitude already exists
        existing_pin = Pins.objects.filter(latitude=lat, longitude=lng).first()
        if existing_pin:
            # Update the existing pin
            existing_pin.title = title
            existing_pin.description = description
            existing_pin.tags = tags
            existing_pin.save()
            return JsonResponse({'status': 'Updated'})
        else:
            # Create a new pin
            pin = Pins(title=title, description=description, latitude=lat, longitude=lng, tags=tags)
            pin.save()
            return JsonResponse({'status': 'Created'})
    elif request.method == 'DELETE':
        if pin_id is not None:
            try:
                pin = Pins.objects.get(pk=pin_id)
            except Pins.DoesNotExist:
                return JsonResponse({'status': 'Not Found'}, status=404)
            pin.delete()
            return JsonResponse({'status': 'Deleted'})
        else:
            return JsonResponse({'status': 'Bad Request: No pin id provided'}, status=400)
    else:
        return JsonResponse({'status': 'Method Not Allowed'}, status=405)

def retrieve_marker(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get('lat')
        lng = data.get('lng')

        # Save the marker to the database
        pin = Pins(title="New Pin", description="New Description", latitude=lat, longitude=lng, tags="New Tag")
        pin.save()

        return JsonResponse({'status': 'success'})


def login(request):
    if request.method == "POST":
        if request.POST["username"] != "" or request.POST["password"] != "":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect("/")
            else:
                if UserAuth.objects.filter(username=username).exists():
                    user = UserAuth.objects.get(username=username)
                    if user.check_password(password):
                        return redirect("")
                    else:
                        return render(request, "login.html", {"error": "Invalid password"})
                else:
                    return render(request, "login.html", {"error": "Invalid username"})

        else:
            return render(request, "login.html", { "error": "Missing username or password"})
            
     

    return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        errors = []
        if request.POST.get("age") != "age":
            errors.append("You have to be 18 years or older to use this service")
        if request.POST["username"] == "":
            errors.append("Username is required")
        if len(request.POST["username"]) > 16:
            errors.append("Username must be less than 16 characters long")
        if request.POST["email"] == "":
            errors.append("Email is required")
        if request.POST["password"] != request.POST["password_confirm"]:
            errors.append("Passwords do not match")
        if UserAuth.objects.filter(username=request.POST["username"]).exists():
            errors.append("Username already exists")
        if UserAuth.objects.filter(email=request.POST["email"]).exists():
            errors.append("Email already exists")
        if errors:
            return render(request, "signup.html", {"errors": errors})
        else:
            user = UserAuth.objects.create_user(
                request.POST["username"],
                request.POST["email"],
                request.POST["password"]
            )
            profile = Profile(user=user)
            user.save()
            profile.save()
            return redirect("login")
    return render(request, "signup.html")

def change_password(request):
    if request.method == "POST":
        errors = []
        if request.POST["old_password"] == "":
            errors.append("Old password is required")
        old_password = request.POST["old_password"]
        user = request.user
        if not user.check_password(old_password):
            return render(request, "change_password.html", {"errors": ["Invalid old password"]})
        if request.POST["new_password"] == "":
            errors.append("New password is required")
        if request.POST["new_password"] != request.POST["new_password_confirm"]:
            errors.append("New passwords do not match")
        if len(request.POST["new_password"]) < 8:
            errors.append("New passwords must atleast be 8 characters long")
        if re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$", request.POST["new_password"]):
            errors.append("New password must contain atleast one uppercase letter, one lowercase letter and one number")
        if errors:
            return render(request, "change_password.html", {"errors": errors})
        else:
            user = UserAuth.objects.get(username=request.user.username)
            user.set_password(request.POST["new_password"])
            user.save()
            return redirect("home")
    return render(request, "change_password.html")

def logout(request):
    django_logout(request)
    return redirect("login")

def pins(request):
    return render(request, "pins.html")
  