from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


visibility_type = {
    ("+", "Public"),
    ("#", "Protected"),
    ("-", "Private"),
}

class PinType(models.TextChoices):
    USER = 'user', 'User'
    MEETUP = 'meetup', 'Meetup'
    PLACE = 'place', 'Place'

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default='blue')
    def __str__(self):
        return self.name
    def create_tag(self, name):
        self.name = name
        self.save()
        return self
    
class Pins(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default='There is no title', max_length=255)
    description = models.TextField(default='There is no description')
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    created_timestamp = models.DateTimeField(default=timezone.now)
    # pin_tags = models.ManyToManyField(Tags, related_name='pin_tags')
    tags = models.CharField(default='none', max_length=255)
    pin_type = models.CharField(
        max_length=10,
        choices=PinType.choices,
        default=PinType.PLACE,
    )

    def __str__(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    biography = models.TextField(default='There is no biography', max_length=2000)
    favorite_tags = models.ManyToManyField(Tags, related_name='favorite_tags')


    
class UserAuth(User):
    def __str___(self):
        return self.username
    pass

