from django.db import models
from django.utils import timezone

class Pins(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default='There is no title', max_length=255)
    description = models.TextField(default='There is no description')
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    created_timestamp = models.DateTimeField(default=timezone.now)
    tags = models.CharField(default='none', max_length=255)

    def __str__(self):
        return self.title
    
class Meetups(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default='There is no title', max_length=255)
    description = models.TextField(default='There is no description')
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    owner_id = models.IntegerField(null=True)
    invited = models.CharField(default='No one', max_length=255)
    tags = models.CharField(default='none', max_length=255)
    created_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title