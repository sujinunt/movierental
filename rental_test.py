import unittest
from rental import Rental
from movie import Movie, PriceCode, MovieCatalog


class RentalTest(unittest.TestCase):

	def setUp(self):
		catalog = MovieCatalog()
		self.new_movie = catalog.get_movie("Loki")
		self.regular_movie = catalog.get_movie("Fifty Shades of Grey")
		self.childrens_movie = catalog.get_movie("Mulan")

		self.price_code_new_movie = PriceCode.for_movie(self.new_movie)
		self.price_code_regular_movie = PriceCode.for_movie(self.regular_movie)
		self.price_code_childrens_movie = PriceCode.for_movie(self.childrens_movie)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie."""
		catalog = MovieCatalog()
		m = catalog.get_movie("Deadpool")
		self.assertEqual("Deadpool", m.get_title())

	def test_rental_price_new_movie(self):
		"""Test rental price when rent new movie."""
		rental = Rental(self.new_movie, 1,  self.price_code_new_movie)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5, self.price_code_new_movie)
		self.assertEqual(rental.get_charge(), 15.0)

	def test_rental_price_regular_movie(self):
		"""Test rental price when rent regular movie."""
		rental = Rental(self.regular_movie, 1, self.price_code_regular_movie)
		self.assertEqual(rental.get_charge(), 2.0)
		rental = Rental(self.regular_movie, 3, self.price_code_regular_movie)
		self.assertEqual(rental.get_charge(), 3.5)

	def test_rental_price_childrens_movie(self):
		"""Test rental price when rent children movie."""
		rental = Rental(self.childrens_movie, 1, self.price_code_childrens_movie)
		self.assertEqual(rental.get_charge(), 1.5)
		rental = Rental(self.childrens_movie, 4, self.price_code_childrens_movie)
		self.assertEqual(rental.get_charge(), 3)

	def test_rental_points_new_movie_more_than_one_day(self):
		"""Test rental point when rent new movie more than one day."""
		rental = Rental(self.new_movie, 5, self.price_code_new_movie)
		self.assertEqual(rental.get_rental_points(), 2)

	def test_rental_points_new_movie_one_day(self):
		"""Test rental point when rent new movie one day."""
		rental = Rental(self.new_movie, 1, self.price_code_new_movie)
		self.assertEqual(rental.get_rental_points(), 1)

	def test_rental_points_not_new_movie(self):
		"""Test rental point when rent not new movie."""
		rental = Rental(self.regular_movie, 5, self.price_code_regular_movie)
		self.assertEqual(rental.get_rental_points(), 1)