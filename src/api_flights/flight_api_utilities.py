import flight_types
from tabulate import tabulate


def print_trips(trips: list[flight_types.RoundTrip]):
    table = []

    for trip in trips:
        dest = str(trip.outbound.destinationFull) + " (" + str(trip.outbound.destination) + ")"
        price = str(round(float(trip.totalPrice), 2))
        out_date = str(trip.outbound.departureTime)
        return_date = str(trip.inbound.departureTime)
        table.append(["Dest:  " + dest, "£" + price, out_date, return_date])

    print(tabulate(table))

