import sys
import time

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from catalog.models import Image, Location


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class Command(BaseCommand):
    help = "Добавляет место в базу из JSON "

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        response = requests.get(options["url"])
        response.raise_for_status()
        place = response.json()

        location, created = Location.objects.get_or_create(
            title=place["title"],
            defaults={
                "short_description": place["description_short"],
                "long_description": place["description_long"],
                "latitude": place["coordinates"]["lat"],
                "longitude": place["coordinates"]["lng"],
            },
        )

        if not created:
            self.stdout.write("Это место уже есть!")
            return

        for order, image_url in enumerate(place["imgs"]):
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                eprint(f"Ошибка {e}")
                continue
            except requests.exceptions.ConnectionError as e:
                eprint(f"Ошибка соединения - {e}.")
                time.sleep(10)
                continue

            filename = image_url.split("/")[-1]

            Image.objects.create(
                location=location,
                order=order,
                file=ContentFile(image_response.content, name=filename),
                alt=filename,
            )

        self.stdout.write("Готово")
