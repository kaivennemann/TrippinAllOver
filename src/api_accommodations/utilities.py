"""
List of accommodation-related functions we would like to have access to for our web app.

"""

from ..utilities.event_calendar import EventCalendar, DateRange
from .accommodation import Accommodation


def get_cheapest_hostels(city: str, dates: DateRange) -> Accommodation:
    # Return a sorted list of the cheapest hostels in given city for that DateRange
    pass