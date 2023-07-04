from flight_api import FlightAPI
from datetime import datetime, timedelta
from flight_api_utilities import print_trips

api = FlightAPI("GBP")

out_day = datetime(2023, 10, 13)
out_range = 2
return_day = out_day + timedelta(days=2)
return_range = 1

trips = api.get_cheapest_trips("STN", out_day, out_range, return_day, 1)



trips.sort(key = lambda f : f.totalPrice)

print_trips(trips)

