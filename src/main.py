
# from api_flights.flight_api import FlightAPI
from utilities.event_calendar import EventCalendar, DateRange, TripLength
from api_flights.flight_api import FlightAPI
from api_flights.flight_api_utilities import print_trips
from datetime import date


api = FlightAPI()

# Method 1
# flights = api.get_cheapest_roundtrips(
#     'STN',
#     DateRange(date(2023,10,10), date(2023,10,13)),
#     DateRange(date(2023,10,16), date(2023,10,19))
# )
# print_trips(flights)

# Method 2
flights = api.get_cheapest_roundtrips(
    'STN',
    EventCalendar.of([(date(2023,10,11), date(2023,10,13))]),
    TripLength(3, 3)
)
print_trips(flights)
