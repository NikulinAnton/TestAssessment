from django.urls import path

from core import views

urlpatterns = [
    path("", views.TrucksView.as_view(), name="core-trucks"),
]
