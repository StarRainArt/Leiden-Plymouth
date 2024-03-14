from django import forms
from .models import Meetups
from YouthSpotsBrain.models import Pins,Profile
class MeetupsForm(forms.ModelForm):
    #define all
    location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # name_meetup = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Meetups
        fields = ['location', 'name_meetup', 'description', 'time_start', 'time_end', 'invited', 'tags', 'pin', 'visibility']

class MeetupsForm_Edit(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_meetup = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.Textarea())
    time_start = forms.DateTimeField(widget=forms.DateTimeInput())
    time_end = forms.DateTimeField(widget=forms.DateTimeInput())
    #invited = forms.CharField(widget=forms.TextInput())
    #tags = forms.CharField(widget=forms.TextInput())
    #visibility = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = Meetups
        fields = ['location', 'name_meetup', 'description', 'time_start', 'time_end', 'invited', 'tags', 'pin', 'visibility']

    
    
