from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("mia_app/", include("mia_app.urls")), # URL per accedere all'app
    path("admin/", admin.site.urls),  # URL per accedere al pannello admin

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)