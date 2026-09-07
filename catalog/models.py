from tkinter import Image

from django.db import models


class Location(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.TextField(max_length=500)
    description_long = models.TextField(max_length=5000)
    coordinates_x = models.FloatField()
    coordinates_y = models.FloatField()
    images = models.ManyToManyField(Image, related_name='locations', blank=True)

class ImageField(models.Model):
    url = models.URLField()
    order = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)