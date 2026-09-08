from django.contrib import admin
from catalog.models import Location, Image
from django.db import models


class ImageInline(admin.TabularInline):
    model = Image

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates_x')
    inlines = [ImageInline]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'order', 'location')


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
