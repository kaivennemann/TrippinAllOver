import ryanair.types
from tabulate import tabulate

def print_flights(flights: list[ryanair.types.Trip]):
    table = []

    for flight in flights:
        dest = str(flight.outbound.destinationFull) + " (" + str(flight.outbound.destination) + ")"
        price = str(round(float(flight.totalPrice), 2))
        table.append(["Dest:", dest, "Price:", "£" + price])

    print(tabulate(table))
