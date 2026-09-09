from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from catalog.models import Location


def get_location_info(request, place_id):
    location = get_object_or_404(Location, id=place_id)
    location_formatted_data = {
        "title": location.title,
        "imgs": [img.file.url for img in location.images.all()],
        "description_short": location.description_short,
        "description_long": location.description_long,
        "coordinates": {
            "lng": location.coordinates_x,
            "lat": location.coordinates_y,
        },
    }
    return JsonResponse(
        location_formatted_data,
        safe=False,
        json_dumps_params={"ensure_ascii": False, "indent": 2},
    )


def show_home(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_x, place.coordinates_y],
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
