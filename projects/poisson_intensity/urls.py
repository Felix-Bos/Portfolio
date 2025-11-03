from django.urls import path

from . import views

urlpatterns = [
    path("", views.project_detail, name="poisson_detail"),
]
