import json
import sys, os
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).resolve().parent.parent.parent)) # TODO: make this temporary fix less janky
from .api_flights.flight_api import FlightAPI
from utilities.event_calendar import EventCalendar, TripLength, DateRange
from .api_flights.flight_api_utilities import print_trips
from datetime import date, datetime

from django.http import JsonResponse
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


SUPPORTED_OUTBOUND_AIRPORTS = {'STN'}
api = FlightAPI()

@api_view(['GET'])
def flight_list(request):
    # Get all the flights currently stored in the database
    # Serialize them and return json
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return JsonResponse({"flights": serializer.data}, safe=False)

# TODO: move everything to the database
@api_view(['GET'])
def single_trip(request):
    outbound_airport = request.GET.get("outbound")
    start_date = request.GET.get("startdate")
    end_date = request.GET.get("enddate")

    return JsonResponse(create_single_trip_json(outbound_airport, start_date, end_date))


def create_single_trip_json(outbound_airport, start_date, end_date):
    if outbound_airport is None or start_date is None or end_date is None:
        return {'error': 'incorrect url parameters'}
    
    if outbound_airport not in SUPPORTED_OUTBOUND_AIRPORTS:
        return {'error': f' {outbound_airport} is not a supported outbound airport. Check format is correct.'}

    date_format = '%Y-%m-%d'

    try:
        start = datetime.strptime(start_date, date_format).date()
    except ValueError:
        return {'error': 'start date has incorrect format.'}

    try:
        end = datetime.strptime(end_date, date_format).date()
    except ValueError:
        return {'error': 'end date has incorrect format.'}

    # TODO: make this line safer (using try except or smthn)
    flights = api.get_cheapest_roundtrips('STN', start, end)

    return {'data': flights}

# TODO: look into this csrf exempt thing
@csrf_exempt 
def calendar(request):
    if request.method == "POST":
        print(type(json.loads(request.body)))

        

    return JsonResponse({})
