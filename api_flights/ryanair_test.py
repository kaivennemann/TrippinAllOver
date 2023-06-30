from ryanair import Ryanair
from datetime import datetime, timedelta
from ryanair_utilities import print_flights

api = Ryanair(currency="GBP")
out_day = datetime(2023, 7, 7)
out_range = 2
return_day = datetime(2023, 7, 10)
return_range = 1

flights = api.get_cheapest_return_flights(source_airport = "STN",
                                    date_from = out_day,
                                    date_to = out_day + timedelta(days = out_range),
                                    return_date_from = return_day,
                                    return_date_to = return_day + timedelta(days = return_range))



flights.sort(key = lambda f : f.totalPrice)

for f in flights[:5]:
    print_flight(f)
