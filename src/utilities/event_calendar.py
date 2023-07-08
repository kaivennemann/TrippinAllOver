'''
This module defines the EventCalendar object, which is useful for specifying date ranges for travel purposes.
'''

from datetime import datetime, timedelta, date


class EventCalendar:

    # Initializes an EventCalendar object with default length of 366 days
    def __init__(self, start: date = datetime.now().date(), end: date = (datetime.now() + timedelta(days=365)).date()):
        if end < start: raise Exception("Invalid range")
        self.start = start
        self.end = end
        self.length = (end - start).days + 1  # +1 to include the end date
        self.events = [False for _ in range(self.length)]  # list of booleans indicating whether a day has an event


    # Returns True if a given date has an event
    def has_event_on_day(self, date: date):
        if not self.__in_range(date): return False
        return self.events[self.__index_of(date)]
    

    # Sets an event on a given date
    def add_event_on_day(self, date: date): self.__set_event(date, True)
    

    # Set an event on a date range
    def add_event(self, start: date, end: date): self.__set_events(start, end, True)


    # Remove event on a given date
    def delete_event_on_day(self, date: date): self.__set_event(date, False)


    # Remove events from a given date range
    def delete_event(self, start: date, end: date): self.__set_events(start, end, False)


    # String representation of EventCalendar object, includes events
    def __str__(self):
        s = f'EventCalendar: start={str(self.start)}, end={str(self.end)}, length={self.length}\nEvents: '
        e = ''
        i = 0
        while i < self.length:
            if self.events[i]:
                d = str(self.start + timedelta(days=i))
                if i == self.length - 1 or not self.events[i+1]:  # event is only one day
                    e += f' [{d}]'
                else:  # event is multiple consecutive days
                    while self.events[i+1]:
                        i += 1
                    d2 = str(self.start + timedelta(days=i))
                    e += f' [{d}, {d2}]'
            i += 1
        if e == '': e = '(N/A)'
        return s + e


    # Raises an Exception if date is not in valid range
    def __check_range(self, date: date):
        if not self.__in_range(date): raise Exception("Date not in range")


    # Private helper method; returns an index into the event list for a given date
    def __index_of(self, date: date): return (date - self.start).days


    # Returns True if given date is in range of this EventCalendar object
    def __in_range(self, date): return (self.start <= date <= self.end)


    # Set date in event list to a value
    def __set_event(self, date: date, val: bool):
        self.__check_range(date)
        self.events[self.__index_of(date)] = val


    # Set dates in event list to a value
    def __set_events(self, start: date, end: date, val: bool):
        self.__check_range(start)
        self.__check_range(end)
        i = self.__index_of(start)
        j = self.__index_of(end)
        for k in range(i, j+1):
            self.events[k] = val


