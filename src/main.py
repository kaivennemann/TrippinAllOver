"""
Ideas:
    - add in a europe booking agency API or something to book hostels
    - figure out how payment card APIs work
    - package everything up as a weekend trip for Cambridge students (flights + hotel + maybe smth extra)

"""


# from api_flights.flight_api import FlightAPI
from utilities.event_calendar import EventCalendar, DateRange, TripLength
from api_flights.flight_api import FlightAPI
from api_flights.flight_api_utilities import print_trips
from datetime import date



def main():

    api = FlightAPI()

    # Method 1
    print(f"Method 1:")
    flights = api.get_cheapest_roundtrips(
        'STN',
        DateRange(date(2023,10,10), date(2023,10,13)),
        DateRange(date(2023,10,16), date(2023,10,19))
    )
    print_trips(flights[:10])
    print()

    # Method 2
    print(f"Method 2:")
    flights = api.get_cheapest_roundtrips('STN', EventCalendar.of([(date(2023,11,5), date(2023,11,8))]), TripLength(2, 3))
    print_trips(flights[:10])
    print()

    # Method 3
    print(f"Method 3:")
    flights = api.get_cheapest_roundtrips('STN', date(2023,11,5), 2, date(2023,11,8), 2)
    print_trips(flights[:10])
    print()



if __name__ == '__main__':
    main()