from rental import Rental
from movie import Movie


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), rental.get_charge())

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", self.get_total_charge())
        statement += "Frequent Renter Points earned: {}\n".format(self.get_total_frequent_renter_points())

        return statement

    def get_total_charge(self):
        total_amount = 0 # total charges
        for rental in self.rentals:
            total_amount += rental.get_charge()
        return total_amount

    def get_total_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self.rentals:
            frequent_renter_points += rental.get_frequent_renter_points()
        return frequent_renter_points


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", Movie.REGULAR)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("CitizenFour", Movie.NEW_RELEASE)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
