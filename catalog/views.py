from django.shortcuts import render, get_object_or_404
from django.templatetags.static import static
from catalog.models import Location
from django.http import HttpResponse
from django.http.response import JsonResponse


def get_location(request, place_id):
    location = get_object_or_404(Location, id=place_id)
    location_formatted_data = {
    "title": location.title,
    "imgs": [
        img.file.url for img in location.images.all()
    ],
    "description_short": location.description_short,
    "description_long": location.description_long,
    "coordinates": {
        "lng": location.coordinates_x,
        "lat": location.coordinates_y,
    }
}
    return JsonResponse(location_formatted_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def show_home(request):
    places = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinates_x, place.coordinates_y]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": static("places/moscow_legends.json")
                }
            }
            for place in Location.objects.all()
        ]
    }
    return render(request, 'index.html', {"places": places})
