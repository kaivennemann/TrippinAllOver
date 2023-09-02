from django.urls import path
from . import views

urlpatterns = [
    path('singletrip/', views.single_trip, name='booking-home'),
]
