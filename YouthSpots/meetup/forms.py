from django import forms
from meetup.models import Meetups
from YouthSpotsBrain.models import Pins
class MeetupsForm(forms.ModelForm):
    #define all
    location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    #name_meetup = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Meetups
        fields = ['location', 'name_meetup', 'description', 'time_start', 'time_end', 'invited', 'tags', 'pin', 'visibility']
