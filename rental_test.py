import unittest
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.normal)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie."""
		m = Movie("CitizenFour", PriceCode.normal)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.normal, m.get_price_code())

	def test_rental_price_new_movie(self):
		"""Test rental price when rent new movie."""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_charge(), 15.0)

	def test_rental_price_regular_movie(self):
		"""Test rental price when rent regular movie."""
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_charge(), 2.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_charge(), 3.5)

	def test_rental_price_childrens_movie(self):
		"""Test rental price when rent children movie."""
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_charge(), 1.5)
		rental = Rental(self.childrens_movie, 4)
		self.assertEqual(rental.get_charge(), 3)

	def test_rental_points_new_movie_more_than_one_day(self):
		"""Test rental point when rent new movie more than one day."""
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_frequent_renter_points(), 2)

	def test_rental_points_new_movie_one_day(self):
		"""Test rental point when rent new movie one day."""
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_frequent_renter_points(), 1)

	def test_rental_points_not_new_movie(self):
		"""Test rental point when rent not new movie."""
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_frequent_renter_points(), 1)