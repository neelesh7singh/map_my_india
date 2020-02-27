from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, blank = True)
    address = models.CharField(max_length = 200)
    interest = models.CharField(max_length = 200)
    latitude = models.CharField(max_length = 100)
    longitude = models.CharField(max_length = 100)
    date = models.CharField(max_length = 20)
