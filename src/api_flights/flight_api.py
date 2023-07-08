"""
This module provides a generic flight API that provides information on flight departures/prices.
As of now, it only incorporates data from Ryanair; however, this could feasibly be extended.
"""

from ryanair import Ryanair
from flight_types import Flight, RoundTrip
from datetime import datetime, timedelta

class FlightAPI:

    # Initialize FlightAPI,
    def __init__(self, currency: str = "GBP"):  # default currency is GBP
        self.currency = currency
        self.ryanair = Ryanair(currency = self.currency)  # Ryanair API

    # Returns a list with the cheapest RoundTrips within a specified date range from a specified origin airport
    def get_cheapest_trips(self, origin: str, out_day: datetime, out_range: int, return_day: datetime, return_range: int):
        result = self.ryanair.get_cheapest_return_flights(
            source_airport = origin,
            date_from = out_day,
            date_to = out_day + timedelta(days = out_range),
            return_date_from = return_day,
            return_date_to = return_day + timedelta(days = return_range)
        )
        return result
    
    # Given a calendar object of some sort (which specifies a set of dates), 
    



