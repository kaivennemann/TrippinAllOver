'''
Tests for EventCalendar object methods. Run from root directory with pytest.
'''

import sys
sys.path.append(sys.path[0][:-5])  # Temporary fix to enable imports from neighboring folder; TODO: replace

import pytest

from src.utilities.event_calendar import EventCalendar
from datetime import datetime, timedelta, date


# TEST CLASSES

class TestEventCalendar:

    start = date(2004, 10, 31)


    def test_init(self, capsys):
        # capsys is built in and allows the method to print to console despite pytest catching our stdout fd
        # For more info: https://buildmedia.readthedocs.org/media/pdf/pytest/latest/pytest.pdf (2.11)
        
        # Initialize and print EventCalendar object
        e = EventCalendar()
        with capsys.disabled(): print(f'Default EventCalendar: {e}')

        # Set and print values to compare e against
        today = datetime.now().date()
        one_year_from_today = today + timedelta(days=364)
        with capsys.disabled(): print(f'Today: {today}\nOne year: {one_year_from_today}')

        # Compare values of e instance vars
        assert e.start == today
        assert e.end == one_year_from_today
        assert e.events.count(False) == 365


    def test_init2(self):
        e = EventCalendar(self.start)

        assert e.start == self.start
        assert e.end == self.start + timedelta(days=364)
        assert e.events.count(False) == 365
    

    def test_adding(self, capsys):
        e = EventCalendar(self.start)
        day0 = self.start
        day3 = self.start + timedelta(days=3)
        day5 = self.start + timedelta(days=5)

        e.add_event_on_day(day0)
        assert e.has_event_on_day(day0)
        assert not e.has_event_on_day(day3)

        e.add_event(day3, day5)
        assert e.events[:8] == [True, False, False, True, True, True, False, False]

        with capsys.disabled(): print(f'{e}')

    
    def test_expanding(self):
        e = EventCalendar(self.start)
        day400 = self.start + timedelta(days=400)
        day_minus1 = self.start + timedelta(days=-1)

        e.add_event_on_day(day400)
        assert e.has_event_on_day(day400)
        assert len(e.events) == 2 * 365
        assert e.start == self.start
        assert e.end == self.start + timedelta(days = 365 + 364)

        e.add_event_on_day(day_minus1)
        assert e.has_event_on_day(day_minus1)
        assert e.start == self.start + timedelta(days = -2 * 365)
        assert e.end == self.start + timedelta(days = 365 + 364)
        assert len(e.events) == 4 * 365



    def test_deleting(self):
        e = EventCalendar(self.start)
        day0 = self.start
        day3 = self.start + timedelta(days=3)
        day4 = self.start + timedelta(days=4)
        day5 = self.start + timedelta(days=5)

        e.add_event_on_day(day0)
        e.add_event(day3, day5)

        e.delete_event_on_day(day3)
        assert not e.has_event_on_day(day3)

        e.delete_event(day0, day4)
        assert not e.has_event_on_day(day0)
        assert not e.has_event_on_day(day3)
        assert not e.has_event_on_day(day4)
        assert e.has_event_on_day(day5)

