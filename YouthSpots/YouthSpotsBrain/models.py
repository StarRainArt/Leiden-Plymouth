from django.db import models

class Pins(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    longitude = models.FloatField()
    latitude = models.FloatField()
    owner_id = models.IntegerField()
    invited = models.CharField(max_length=255)
    created_timestamp = models.DateTimeField()

    def __str__(self):
        return self
    
class Meetups(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    tags = models.ManyToManyField('Tag')
    longitude = models.FloatField()
    latitude = models.FloatField()
    owner_id = models.IntegerField()
    invited = models.CharField(max_length=255)
    created_timestamp = models.DateTimeField()

    def __str__(self):
        return self
