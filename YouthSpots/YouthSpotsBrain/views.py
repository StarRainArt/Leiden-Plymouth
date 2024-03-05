from django.shortcuts import render
from YouthSpotsBrain.models import EVCharcinglocation

# Create your views here.
def home(request):
    return render(request, "home.html")

def maps(request):
    stations = list(EVCharcinglocation.objects.values('latitude', 'longitude')[:100])
    print(stations[:2])
    context = {'stations':stations}
    return render(request, "maps.html", context)
