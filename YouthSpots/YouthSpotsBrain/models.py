from django.db import models

type_mt = {
    "FC": "Fan_cosplay",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
}

visibility_type = {
    "+": "Public",
    "#": "Protected",
    "-": "Private",
}

class MeetupData(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_meetup = models.CharField(max_length=30)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    description = models.CharField(max_length=255)
    type_meetup = models.CharField(max_length=10, choices=type_mt, default='FC')
    location_meetup = models.BigIntegerField()
    pins = models.BigIntegerField()
    visibility = models.CharField(max_length=10, choices=visibility_type, default='-')

class MeetupUserData(models.Model):
    id = models.BigAutoField(primary_key=True)
    meeting_id = models.ForeignKey(MeetupData, on_delete=models.CASCADE) 
    # ForeignKey to MeetupData model
    # User information can be added later
    visibility = models.BooleanField()