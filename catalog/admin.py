from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from catalog.models import Image, Location


class ImageInline(SortableStackedInline, admin.TabularInline):
    model = Image
    readonly_fields = ["image_preview"]
    autocomplete_fields = ["location"]
    fields = ["file", "image_preview", "order"]

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 300px;">', obj.file.url)


class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview", "order"]
    list_display = ["file", "image_preview", "order"]

    def image_preview(self, obj):
        return format_html('<img src="{}" height={}>', obj.file.url, 200)



admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
