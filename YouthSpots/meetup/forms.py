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
    # name_meetup = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter meetup name'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description'}))
    # time_start = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))
    # time_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}))
    # invited = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter invited people'}))
    # tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter tags'}))
    # pin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter pin'}))
    # visibility = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter visibility'}))
    class Meta:
        model = Meetups
        fields = ['location', 'name_meetup', 'description', 'time_start', 'time_end', 'invited', 'tags', 'pin', 'visibility']

    
    
