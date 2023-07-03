from ryanair import Ryanair
from datetime import datetime, timedelta
from ryanair_utilities import print_trips

api = Ryanair(currency="GBP")
out_day = datetime(2023, 10, 13)
out_range = 2
return_day = out_day + timedelta(days=2)
return_range = 1

trips = api.get_cheapest_return_flights(source_airport = "STN",
                                    date_from = out_day,
                                    date_to = out_day + timedelta(days = out_range),
                                    return_date_from = return_day,
                                    return_date_to = return_day + timedelta(days = return_range))

flights = api.get_cheapest_flights(airport = "STN",
                                    date_from = out_day,
                                    date_to = out_day + timedelta(days = out_range))


trips.sort(key = lambda f : f.totalPrice)

print_trips(trips)

