from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("mia_app/", include("mia_app.urls")),
    path("admin/", admin.site.urls),
]