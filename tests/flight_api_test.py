'''
Tests for FlightAPI methods. Run from root directory with pytest.
'''


import sys
sys.path.append(sys.path[0][:-5])  # Temporary fix to enable imports from neighboring folder; TODO: replace

import pytest

from src.api_flights.flight_api import FlightAPI
from src.api_flights.flight_api_utilities import print_trips
from src.utilities.event_calendar import DateRange
from datetime import date


class TestFlightAPI:

    def test_get_cheapest_roundtrips(self, capsys):
        api = FlightAPI()

        # Method 1
        flights = api.get_cheapest_roundtrips(
            'STN',
            DateRange(date(2023,10,10), date(2023,10,13)),
            DateRange(date(2023,10,16), date(2023,10,19))
        )
        print_trips(flights[:10])

        # Method 2
