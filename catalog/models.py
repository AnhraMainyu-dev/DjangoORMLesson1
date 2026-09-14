from django.db import models
from tinymce.models import HTMLField


class Image(models.Model):
    file = models.ImageField(
        upload_to="images/", verbose_name="Путь к файлу изображения"
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name="Порядок отображения на странице локации"
    )
    alt = models.CharField(max_length=200, blank=True, verbose_name="Имя файла")
    location = models.ForeignKey(
        "Location",
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Локация, к которой изображение привязано",
    )

    class Meta:
        ordering = ["order"]
        indexes = [
            models.Index(fields=["order"]),
        ]

    def __str__(self):
        return f"{self.file}"


class Location(models.Model):
    title = models.CharField(max_length=150, verbose_name="Имя локации")
    short_description = models.TextField(
        blank=True, verbose_name="Короткое описание локации"
    )
    long_description = HTMLField(blank=True, verbose_name="Полное описание локации")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("title", "latitude", "longitude")
