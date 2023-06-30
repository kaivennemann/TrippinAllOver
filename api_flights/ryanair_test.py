from ryanair import Ryanair
from datetime import datetime, timedelta

api = Ryanair(currency="GBP")
day1 = datetime.today().date()
day2 = day1 + timedelta(days=1)

flights = api.get_cheapest_flights("STN", day1, day1)

f = flights[0]
print(f)