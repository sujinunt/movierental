class Movie:
	"""
	A movie available for rent.
	"""
	# The types of movies (price_code). 
	REGULAR = 0
	NEW_RELEASE = 1
	CHILDRENS = 2
	
	def __init__(self, title, price_code):
		# Initialize a new movie. 
		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def get_title(self):
		return self.title
	
	def __str__(self):
		return self.title
