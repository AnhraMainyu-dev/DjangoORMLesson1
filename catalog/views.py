from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from catalog.models import Location


def get_location_info(request, place_id):
    location = get_object_or_404(Location, id=place_id)
    location_details = {
        "title": location.title,
        "imgs": [img.file.url for img in location.images.all()],
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {
            "lng": location.latitude,
            "lat": location.longitude,
        },
    }
    return JsonResponse(
        location_details,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )


def show_home_page(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.latitude, place.longitude],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse("place_info", args=[place.id]),
                },
            }
            for place in Location.objects.all()
        ],
    }
    return render(request, "index.html", {"places": places})
