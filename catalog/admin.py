from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from catalog.models import Location, Image
from django.db import models


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']
    fields = ['file', 'order', 'image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{}" height={}>',
                           obj.file.url,
                           200)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates_x')
    inlines = [ImageInline]

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']
    list_display = ('file', 'order', 'image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" height={}>',
                           obj.file.url,
                           200)


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
