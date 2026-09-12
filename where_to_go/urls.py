from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from catalog.views import get_location_info, show_home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", show_home_page),
    path("places/<int:place_id>/", get_location_info, name="place_info"),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
