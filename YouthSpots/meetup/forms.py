from django import forms
from .models import Meetups

class MeetupsForm(forms.ModelForm):
    class Meta:
        model = Meetups
        fields = [
            'location', 
            'name_meetup', 
            'description', 
            'time_start', 
            'time_end', 
            'owner', 
            'invited', 
            'tags', 
            'created_timestamp', 
            'pin', 
            'visibility'
        ]