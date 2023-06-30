from ryanair import Ryanair
from datetime import datetime, timedelta

api = Ryanair(currency="GBP")
day1 = datetime.today().date()
day2 = day1 + timedelta(days=3)

flights = api.get_cheapest_return_flights(source_airport = "STN",
                                    date_from = day1,
                                    date_to = day1,
                                    return_date_from = day2,
                                    return_date_to = day2)

f = flights
# f.sort(key = lambda x : x.totalPrice)

for x in f[:10]:
    print(str(x) + '\n')