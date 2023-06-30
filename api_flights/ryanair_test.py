from ryanair import Ryanair
from datetime import datetime, timedelta
from ryanair_utilities import print_flights

api = Ryanair(currency="GBP")
day1 = datetime.today().date()
day2 = day1 + timedelta(days=3)

flights = api.get_cheapest_return_flights(source_airport="STN",
                                          date_from=day1,
                                          date_to=day1,
                                          return_date_from=day2,
                                          return_date_to=day2)

# flights.sort(key = lambda x : x.totalPrice)
f = flights[0]
print_flights(flights)
