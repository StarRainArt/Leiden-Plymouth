from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from YouthSpotsBrain.models import Meetups
from YouthSpotsBrain.models import Pins
from django.shortcuts import render, redirect
from YouthSpotsBrain.models import UserAuth
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from geopy.distance import geodesic
import json

def home(request):
    if request.user.is_authenticated == False:
        return redirect("login")
    return render(request, "home.html")

def maps(request):
    return render(request, "maps.html")

def getPins(request):
    return JsonResponse(list(Pins.objects.values('id', 'title', 'description', 'latitude', 'longitude', 'tags', 'created_timestamp')[:100]), safe=False)

def nearest_pin(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    user_location = (latitude, longitude)
    pin_distances = {}

    for pin in Pins.objects.all()[:100]:
        pin_location = (pin.latitude, pin.longitude)
        distance = geodesic(user_location, pin_location).km
        pin_distances[distance] = { 'location': pin_location, 'distance': distance }

    if pin_distances:
        min_distances = min(pin_distances)
        pin_coords = pin_distances[min_distances]
    else:
        min_distances = None
        pin_coords = None

    return JsonResponse({
        'coordinates': pin_coords,
        'distance': min_distances
    })


def save_marker(request):
    if request.method == 'POST':
        print("Received POST request")
        try:
            data = json.loads(request.body)
            print("Received data:", data)
            lat = data.get('lat')
            lng = data.get('lng')

            # Save the marker data as JSON
            marker_data = {'lat': lat, 'lng': lng}
            return JsonResponse(marker_data)
        except Exception as e:
            print("Error processing request:", e)
            return HttpResponse("Error processing request", status=500)
    else:
        return HttpResponse("Invalid request method", status=400)

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
                return redirect("home")
            else:
                if UserAuth.objects.filter(username=username).exists():
                    user = UserAuth.objects.get(username=username)
                    if user.check_password(password):
                        return render(request, "home.html")
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
            user.save()
            return redirect("login")
    return render(request, "signup.html")

def logout(request):
    django_logout(request)
    return redirect("login")

