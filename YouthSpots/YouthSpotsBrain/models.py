from django.db import models
from django.contrib.auth.models import User

class EVCharcinglocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name
    
class UserAuth(User):
    def __str__(self):
        return self.username
