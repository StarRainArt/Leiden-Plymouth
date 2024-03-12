from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

visibility_type = {
    ("+", "Public"),
    ("#", "Protected"),
    ("-", "Private"),
}

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

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def create_tag(self, name):
        self.name = name
        self.save()
        return self

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    biography = models.TextField(default='There is no biography', max_length=2000)
    favorite_tags = models.ManyToManyField(Tags, related_name='favorite_tags')

class Meetups(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default='There is no title', max_length=255)
    description = models.TextField(default='There is no description')
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    longitude = models.FloatField(null = True)
    latitude = models.FloatField(null = True)
    #owner_id = models.OneToOneField(Profile, on_delete=models.CASCADE) non edited version
    owner_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    invited = models.ManyToManyField(Profile, related_name='invited')
    tags = models.CharField(default='none', max_length=255)
    created_timestamp = models.DateTimeField(default=timezone.now)
    pin = models.ForeignKey(Pins, blank=True, null=True, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=10, choices=visibility_type, default='Private')

    def __str__(self):
        return self.title
    
class UserAuth(User):
    def __str___(self):
        return self.username
    pass

