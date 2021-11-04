import re
import unittest 
from customer import Customer
from rental import Rental
from movie import PriceCode, MovieCatalog

class CustomerTest(unittest.TestCase):
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:

		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		catalog = MovieCatalog()
		self.new_movie = catalog.get_movie("Loki")
		self.regular_movie = catalog.get_movie("Fifty Shades of Grey")
		self.childrens_movie = catalog.get_movie("Mulan")

		self.price_code_new_movie = PriceCode.for_movie(self.new_movie)
		self.price_code_regular_movie = PriceCode.for_movie(self.regular_movie)
		self.price_code_childrens_movie = PriceCode.for_movie(self.childrens_movie)

	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass

	def test_statement(self):
		stmt = self.c.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, self.price_code_new_movie))
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
