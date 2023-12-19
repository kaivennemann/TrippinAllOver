from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('flights/', views.flight_list),
    path('singletrip/', views.single_trip, name='single-trip'),
]
