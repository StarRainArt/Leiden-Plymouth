from django.db import models
#type need to be changed or extended
type_mt = {
    ("CE", "Community Event"),
    ("SG", "Social Gathering"),
    ("EE", "Entertainment Event"),
    ("AC", "Activity Club"),
    ("WC", "Workshop/Class"),
    ("FE", "Fitness Event"),
    ("VO", "Volunteer Opportunity"),
    ("TE", "Tech Event"),
    ("ME", "Music Event"),
    ("DE", "Dance Event"),
}

visibility_type = {
    ("+", "Public"),
    ("#", "Protected"),
    ("-", "Private"),
}

class MeetupData(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_meetup = models.CharField(max_length=30)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    description = models.CharField(max_length=255)
    type_meetup = models.CharField(max_length=35, choices=type_mt, default='CE')
    #latitude = models.BigIntegerField()
    #longitude = models.BigIntegerField()
    #meetup_location = models.BigIntegerField()
    #pins = models.BigIntegerField()
    visibility = models.CharField(max_length=10, choices=visibility_type, default='Private')

class MeetupUserData(models.Model):
    id = models.BigAutoField(primary_key=True)
    meeting_id = models.ForeignKey(MeetupData, on_delete=models.CASCADE) 
    # ForeignKey to MeetupData model
    # User information can be added later
    visibility = models.BooleanField()
