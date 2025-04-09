from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
                  # ex: /mia_app/5/
    path("<int:question_id>/", views.detail, name="detail"),
                  # ex: /mia_app/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
                  # ex: /mia_app/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)