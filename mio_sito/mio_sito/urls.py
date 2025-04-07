from django.contrib import admin
from django.urls import include, path

from django.conf import settings            # Da aggiungere
from django.conf.urls.static import static  # Da aggiungere

urlpatterns = [
    path("mia_app/", include("mia_app.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Da aggiungere