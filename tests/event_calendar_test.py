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
    end = date(2004, 11, 7)


    def test_init(self, capsys):
        # capsys is built in and allows the method to print to console despite pytest catching our stdout fd
        # For more info: https://buildmedia.readthedocs.org/media/pdf/pytest/latest/pytest.pdf (2.11)
        
        # Initialize and print EventCalendar object
        e = EventCalendar()
        with capsys.disabled(): print(f'Default EventCalendar: {e}')

        # Set and print values to compare e against
        today = datetime.now().date()
        one_year_from_today = today + timedelta(days=365)
        with capsys.disabled(): print(f'Today: {today}\nOne year: {one_year_from_today}')

        # Compare values of e instance vars
        assert e.start == today
        assert e.end == one_year_from_today
        assert e.length == 366
        assert e.events.count(False) == 366


    def test_init2(self):
        e = EventCalendar(self.start, self.end)

        assert e.start == self.start
        assert e.end == self.end
        assert e.length == 8
        assert e.events.count(False) == 8
    

    def test_adding(self, capsys):
        e = EventCalendar(self.start, self.end)
        day0 = self.start
        day3 = self.start + timedelta(days=3)
        day5 = self.start + timedelta(days=5)
        day8 = self.start + timedelta(days=8)

        e.add_event_on_day(day0)
        assert e.has_event_on_day(day0)
        assert e.events[0]
        assert not e.has_event_on_day(day3)
        with pytest.raises(Exception): e.add_event_on_day(day8)

        e.add_event(day3, day5)
        assert e.events == [True, False, False, True, True, True, False, False]

        with capsys.disabled(): print(f'{e}')


    def test_deleting(self, capsys):
        e = EventCalendar(self.start, self.end)
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

        with capsys.disabled(): print(f'{e}')




