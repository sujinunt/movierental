from enum import Enum
import pandas as pd
import datetime
from typing import List


class Movie:
	"""
	A movie available for rent.
	"""

	def __init__(self, title, year, genre: List[str]):
		# Initialize a new movie.
		self.title = title
		self.year = year
		self.genre = genre

	def get_title(self):
		return self.title

	def get_year(self):
		return self.year

	def get_genre(self):
		return self.genre

	def is_genre(self, genre):
		for movie_genre in self.genre:
			if(genre==movie_genre):
				return True
		return False

	def __str__(self):
		return self.title


class MovieCatalog:
	"""A Movie Catalog of movie that can be rent"""

	def get_movie(self, title: str):
		"""Get movie from csv."""
		data = pd.read_csv("movies.csv")
		movie_query = data.query(f'`title` == "{title}"')
		movie_title = str(movie_query.iloc[0]['title'])
		movie_year = str(movie_query.iloc[0]['year'])
		movie_genre = str(movie_query.iloc[0]['genres']).split('|')
		return Movie(movie_title, movie_year, movie_genre)


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

	def for_movie(movies: Movie):
		"""Price code for movie."""
		year = datetime.date.today().year
		if(movies.get_year()==str(year)):
			return PriceCode.new_release
		elif('Children' in movies.get_genre()):
			return PriceCode.childrens
		else:
			return PriceCode.normal
