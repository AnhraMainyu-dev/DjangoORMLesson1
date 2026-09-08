from django.db import models
from tinymce.models import HTMLField

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    order = models.IntegerField(blank=True, null=True)
    alt = models.CharField(max_length=200, blank=True)
    location = models.ForeignKey('Location', related_name='images', on_delete=models.CASCADE)
    class Meta:
        ordering = ['order']

class Location(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.TextField(max_length=500)
    description_long = HTMLField(max_length=5000)
    coordinates_x = models.FloatField()
    coordinates_y = models.FloatField()

