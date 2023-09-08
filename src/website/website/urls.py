"""
URL configuration for website project.

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
        - include() chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# TODO: can add kwargs and names later (naming lets us refer to the URL unambiguously from elsewhere, e.g. in templates)
urlpatterns = [
    path("", include("booking.urls")),
    path("polls/", include("polls.urls")),
    path('flightsapi/', include("flightsapi.urls")),
    path('admin/', admin.site.urls)
]
