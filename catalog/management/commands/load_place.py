import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from catalog.models import Image, Location


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
                "description_short": place["description_short"],
                "description_long": place["description_long"],
                "coordinates_x": place["coordinates"]["lng"],
                "coordinates_y": place["coordinates"]["lat"],
            },
        )

        if not created:
            self.stdout.write("Это место уже есть!")
            return

        for order, image_url in enumerate(place["imgs"]):
            image = requests.get(image_url)
            image.raise_for_status()
            filename = image_url.split("/")[-1]

            image = Image(location=location, order=order, alt=filename)
            image.file.save(filename, ContentFile(image.content), save=True)

        self.stdout.write("Готово")
