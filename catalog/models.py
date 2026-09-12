from django.db import models
from tinymce.models import HTMLField


class Image(models.Model):
    file = models.ImageField(upload_to="images/", verbose_name="Путь к файлу изображения")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения на странице локации")
    alt = models.CharField(max_length=200, blank=True, verbose_name="Текстовое описание изображения")
    location = models.ForeignKey(
        "Location", related_name="images", on_delete=models.CASCADE, verbose_name="Локация, к которой изображение привязано")

    class Meta:
        ordering = ["order"]
        indexes = [
            models.Index(fields=["order"]),
        ]

    def __str__(self):
        return f"{self.file}"


class Location(models.Model):
    title = models.CharField(max_length=150, verbose_name="Имя локации")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Короткое описание локации")
    long_description = HTMLField(max_length=5000, blank=True, verbose_name="Полное описание локации")
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.title}"

