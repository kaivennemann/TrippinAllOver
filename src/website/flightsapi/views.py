from django.http import JsonResponse

from pathlib import Path
import sys, os

# temporary fix TODO: make this less janky
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(os.path.join(BASE_DIR))
# don't worry if there are red underlines, this stuff does work
from api_flights.flight_api import FlightAPI
from utilities.event_calendar import EventCalendar, TripLength, DateRange
from api_flights.flight_api_utilities import print_trips
from datetime import date, datetime

SUPPORTED_OUTBOUND_AIRPORTS = {'STN'}
api = FlightAPI()


def single_trip(request):
    outbound_airport = request.GET.get("outbound")
    start_date = request.GET.get("startdate")
    end_date = request.GET.get("enddate")

    return JsonResponse(create_single_trip_json(outbound_airport, start_date, end_date))


def create_single_trip_json(outbound_airport, start_date, end_date):
    if outbound_airport is None or start_date is None or end_date is None:
        return {'error': 'incorrect url parameters'}
    else:
        if outbound_airport not in SUPPORTED_OUTBOUND_AIRPORTS:
            return {'error': f' {outbound_airport} is not a supported outbound airport. Check format is correct.'}

        date_format = '%Y-%m-%d'

        start = datetime.strptime(start_date, date_format).date()
        end = datetime.strptime(end_date, date_format).date()

        flights = api.get_cheapest_roundtrips('STN', start, end)

        return {
            'data': flights
                }
