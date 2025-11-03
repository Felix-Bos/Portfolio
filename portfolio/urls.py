"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path

from . import views

portfolio_patterns = [
    path("", views.project_list, name="project_list"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path(
        "projects/",
        include((portfolio_patterns, "portfolio"), namespace="portfolio"),
    ),
    path(
        "projects/alm_durability/",
        include("projects.alm_durability.urls"),
    ),
    path(
        "projects/poisson_intensity/",
        include("projects.poisson_intensity.urls"),
    ),
    path("chatbot/", include("chatbot.urls")),
]
