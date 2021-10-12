import logging
from enum import Enum


class PriceCode(Enum):
	"""An enumeration for different kinds of movies and their behavior"""

	normal = {"price": lambda days:2+(1.5*(days-2)),
	"frp":lambda days: days}
	new_release = {"price": lambda days:3*days,
	"frp":lambda days: days}
	childrens = {"price": lambda days:1.5+(1.5*(days-3)),
	"frp":lambda days: days}

	def __str__(self):
		return self.name

	def price(self, days:int) -> float:
		"""Return the rental price for a given number of days"""
		if(str(self.name)=='normal'):
			pricing=2
			if(days>2):
				pricing = self.value["price"]
				return pricing(days)
		elif(str(self.name)=='childrens'):
			pricing=1.5
			if(days>3):
				pricing = self.value["price"]
				return pricing(days)
		elif(str(self.name)=='new_release'):
			pricing = self.value["price"]
			return pricing(days)
		return pricing

	def frequent_renter_points(self, days:int):
		if(str(self.name)=='new_release' and days > 1):
			return 2
		else:
			return 1


class Movie:
	"""
	A movie available for rent.
	"""

	def __init__(self, title, price_code: PriceCode):
		# Initialize a new movie.
		if not isinstance(price_code, PriceCode):
			log = logging.getLogger()
			log.error(f"Movie {self.get_title()} has unrecognized priceCode {self.get_price_code()}")

		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code

	def get_title(self):
		return self.title

	def __str__(self):
		return self.title

	def get_charge(self, days_rented):
		return self.get_price_code().price(days_rented)

	def get_frequent_renter_points(self, days_rented):
		return self.get_price_code().frequent_renter_points(days_rented)
