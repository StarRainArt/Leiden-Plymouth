from django.db import models
from django.utils import timezone
from YouthSpotsBrain.models import Profile, Pins, visibility_type

class Meetups(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200)
    name_meetup = models.CharField(max_length=255)
    description = models.TextField(default='There is no description')
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    # owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    invited = models.ManyToManyField(Profile, related_name='invited')
    tags = models.CharField(default='none', max_length=255)
    created_timestamp = models.DateTimeField(default=timezone.now)
    pin = models.ForeignKey(Pins, blank=True, null=True, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10, choices=visibility_type, default='Private')
    
    class Meta:
        ordering = ['-created_timestamp']
    
    def __str__(self):
        return self.name_meetup