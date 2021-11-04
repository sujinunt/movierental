import logging
from movie import PriceCode
class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
	field is used.
	"""

	def __init__(self, movie, days_rented, price_code: PriceCode):
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		if not isinstance(price_code, PriceCode):
			log = logging.getLogger()
			log.error(f"Movie {self.get_title()} has unrecognized priceCode {self.price_code}")

		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code

	def get_title(self):
		return self.movie

	def get_charge(self):
		return self.price_code.price(self.days_rented)

	def get_rental_points(self):
		return self.price_code.frequent_renter_points(self.days_rented)
