from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from catalog.models import Location, Image
from django.db import models
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    readonly_fields = ['image_preview']
    fields = ['file', 'image_preview', 'order']

    def image_preview(self, obj):
        return format_html('<img src="{}" height={}>',
                           obj.file.url,
                           200)


class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'coordinates_x')
    inlines = [ImageInline]

class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['image_preview']
    list_display = ('file', 'image_preview', 'order')

    def image_preview(self, obj):
        return format_html('<img src="{}" height={}>',
                           obj.file.url,
                           200)


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
