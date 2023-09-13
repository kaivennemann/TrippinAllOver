from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('singletrip/', views.single_trip, name='single-trip'),
]
