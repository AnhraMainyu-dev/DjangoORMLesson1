"""
URL configuration for Lesson1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from catalog.views import get_location_info, show_home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", show_home),
    path("places/<int:place_id>/", get_location_info, name="place_info"),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
