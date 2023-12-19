'''
This module defines the EventCalendar object, which is useful for specifying date ranges for travel purposes.
'''

from datetime import datetime, timedelta, date


class EventCalendar:

    # Initializes an EventCalendar object with default length of 365 days starting today
    def __init__(self, start = datetime.now().date()):
        self.start = start
        self.end = self.start + timedelta(days=364)
        length = (self.end - self.start).days + 1  # +1 to include today
        self.events = [False for _ in range(length)]  # list of booleans indicating whether a day has an event


    # Create EventCalendar
    @staticmethod
    def of(events):

        event_cal = EventCalendar()
        for d in events:
            if type(d) is date:  # event is one day
                event_cal.add_event_on_day(d)
            else:
                (start, end) = d
                event_cal.add_event(start, end)
        return event_cal


    # Returns a list of DateRange objects corresponding to all the events in the EventCalendar
    def get_events(self):
        event_dateranges = []
        i = 0
        length = len(self.events)
        while i < length:
            if self.events[i]:
                first = self.start + timedelta(days=i)
                while i < length - 1 and self.events[i + 1]:
                    i += 1
                last = self.start + timedelta(days=i)
                event_dateranges.append(DateRange(first, last))
            i += 1
        return event_dateranges
    

    # Returns a list of dates corresponding to days on which an event occurs
    def get_event_days(self):
        event_days = []
        for i in range(len(self.events)):
            if self.events[i]:
                event_day = self.start + timedelta(days = i)
                event_days.append(event_day)
        return event_days
    

    # Returns True if a given date has an event
    def has_event_on_day(self, date: date):
        if not (self.start <= date <= self.end): return False
        return self.events[self.__index_of(date)]
    

    # Sets an event on a given date
    def add_event_on_day(self, date: date): self.__set_event(date, True)
    

    # Set an event on a date range
    def add_event(self, start: date, end: date): self.__set_events(start, end, True)


    # Remove event on a given date
    def delete_event_on_day(self, date: date): self.__set_event(date, False)


    # Remove events from a given date range
    def delete_event(self, start: date, end: date): self.__set_events(start, end, False)


    # Private helper method; returns an index into the event list for a given date
    def __index_of(self, date: date): return (date - self.start).days


    # Set date in event list to a value
    def __set_event(self, date: date, val: bool):
        self.__expand_if_necessary(date)
        self.events[self.__index_of(date)] = val


    # Set dates in event list to a value
    def __set_events(self, start: date, end: date, val: bool):
        self.__expand_if_necessary(start)
        self.__expand_if_necessary(end)
        i = self.__index_of(start)
        j = self.__index_of(end)
        for k in range(i, j+1):
            self.events[k] = val


    # Expand EventCalendar if a date is not in current range
    def __expand_if_necessary(self, date: date):
        while self.__index_of(date) < 0:  # date predates the current range
            length = len(self.events)
            self.events = [False for _ in range(len(self.events))] + self.events
            self.start += timedelta(days = -length)
        while self.__index_of(date) >= len(self.events):  # date is after the current range
            length = len(self.events)
            self.events += [False for _ in range(length)]
            self.end += timedelta(days = length)


    # String representation of EventCalendar object, includes events
    def __str__(self):
        s = f'EventCalendar: start={str(self.start)}, end={str(self.end)}\nEvents: '
        e = ''
        i = 0
        length = len(self.events)
        while i < length:
            if self.events[i]:
                d = str(self.start + timedelta(days=i))
                if i == length - 1 or not self.events[i+1]:  # event is only one day
                    e += f' ({d})'
                else:  # event is multiple consecutive days
                    while self.events[i+1]:
                        i += 1
                    d2 = str(self.start + timedelta(days=i))
                    e += f' ({d}, {d2})'
            i += 1
        if e == '': e = '(N/A)'
        return s + e


class DateRange:

    def __init__(self, first: date, last: date):
        self.first = first
        self.last = last
    

class TripLength:

    def __init__(self, minimum: int, maximum: int):
        self.minimum = minimum
        self.maximum = maximum