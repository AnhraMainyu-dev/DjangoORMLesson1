from django.contrib import admin
from catalog.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates_x')

# Register your models here.
admin.site.register(Location, LocationAdmin)
