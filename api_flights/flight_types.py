from collections import namedtuple

Flight = namedtuple("Flight", ("departureTime", "flightNumber", "price", "currency", "origin", "originFull",
                               "destination", "destinationFull"))
RoundTrip = namedtuple("RoundTrip", ("totalPrice", "outbound", "inbound"))
