from django import forms
from .models import Meetups
from YouthSpotsBrain.models import Pins,Profile
class MeetupsForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # name_meetup = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Meetups
        fields = ['location', 'name_meetup', 'description', 'time_start', 'time_end', 'invited', 'tags', 'pin', 'visibility']
