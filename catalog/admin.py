from django.contrib import admin
from catalog.models import Location, Image


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates_x')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'order', 'location')


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
