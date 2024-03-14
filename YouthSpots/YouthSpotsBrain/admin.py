from django.contrib import admin
from .models import Pins, Tags, Profile, UserAuth
from meetup.models import Meetups
admin.site.register(Pins)
admin.site.register(Tags)
admin.site.register(Profile)
admin.site.register(Meetups)
admin.site.register(UserAuth)


# Register your models here.
