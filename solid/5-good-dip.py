from mock import Mock


class Airline:

    def book(self, origin, destination, data):
        return True

    def get_flights(self, date):
        pass


class FlightBooker:

    def __init__(self, airline, origin, destination):
        self.airline = airline
        self.origin = origin
        self.destination = destination

    def book_two_way(self, start_date, return_date):
        # Note: the definition for Airline.book is Airline.book(from, to, date)
        self.airline.book(self.origin, self.destination, start_date)
        self.airline.book(self.destination, self.origin, return_date)

    def book_one_way(self, date):
        self.airline.book(self.origin, self.destination, date)


def test_one_way_booker():
    airline = Mock(Airline)
    booker = FlightBooker(airline, 'here', 'there')
    booker.book_one_way('18 May 2015')
    assert ('here', 'there') in airline.get_flights('18 May 2015')


def test_two_way_booker():
    airline = Mock(Airline)
    booker = FlightBooker(airline, 'here', 'there')
    booker.book_two_way('18 May 2015', '7 August 2015')
    assert ('here', 'there') in airline.get_flights('18 May 2015')
    assert ('there', 'here') in airline.get_flights('7 August 2015')
