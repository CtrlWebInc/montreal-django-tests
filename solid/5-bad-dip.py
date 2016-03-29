class Airline:

    def book(self, origin, destination, date):
        pass


class FlightBooker:

    def __init__(self, starting_point, destination):
        self.airline = Airline()
        self.origin = starting_point
        self.destination = destination

    def book_two_way(self, start_date, return_date):
        # Note: the definition for Airline.book is Airline.book(from, to, date)
        self.airline.book(self.origin, self.destination, start_date)
        self.airline.book(self.destination, self.origin, return_date)

    def book_one_way(self, date):
        self.airline.book(self.origin, self.destination, date)
