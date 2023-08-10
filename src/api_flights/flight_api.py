"""
This module provides a generic flight API that provides information on flight departures/prices.
As of now, it only incorporates data from Ryanair; however, this could feasibly be extended.
"""

import ryanair
from datetime import datetime, timedelta
from utilities.event_calendar import EventCalendar, DateRange, TripLength
from multimethod import multimeta  # for method overloading


class FlightAPI(metaclass=multimeta):  # allows method overloading

    # Initialize FlightAPI,
    def __init__(self, currency: str = "GBP"):  # default currency is GBP
        self.currency = currency
        self.ryanair = ryanair.Ryanair(currency = self.currency)  # Ryanair API


    # Returns a list with the cheapest RoundTrips within a specified date range from a specified origin airport
    def get_cheapest_roundtrips(self, origin: str, out_days: DateRange, return_days: DateRange):
        result = self.ryanair.get_cheapest_return_flights(
            source_airport = origin,
            date_from = out_days.first,
            date_to = out_days.last,
            return_date_from = return_days.first,
            return_date_to = return_days.last
        )
        return result


    # Takes an EventCalendar of possible departure dates and trip length; returns cheapest roundtrips
    def get_cheapest_roundtrips(self, origin: str, out_days: EventCalendar, trip_length: TripLength):
        days = out_days.get_event_days()
        results = set()
        for day in days:
            return_date_from = day + timedelta(days = trip_length.minimum)
            return_date_to = day + timedelta(days = trip_length.maximum)
            return_days = DateRange(return_date_from, return_date_to)
            cheapest = self.get_cheapest_roundtrips(origin, DateRange(day, day), return_days)
            for roundtrip in cheapest:
                results.add(roundtrip)
        return sorted(list(results))    


    def get_cheapest_roundtrips(self, origin: str, out_day: datetime, out_range: int, return_day: datetime, return_range: int):
        out_days = DateRange(out_day, out_day + timedelta(days = out_range))
        return_days = DateRange(return_day, return_day + timedelta(days = return_range))
        return self.get_cheapest_roundtrips(origin, out_days, return_days)
    
    



