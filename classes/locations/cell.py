from classes.tech.colors 	import Colors
from random					import randint, choice
c = Colors()

class Cell:
	def __init__(self, x, y, size):
		self.x, self.y	= x, y
		self.size		= size
		self.status		= choice(('earth', 'water', 'abyss'))
		if   self.status == 'earth': self.color = choice((c.GREEN, c.WHITE, c.ORANGE))
		elif self.status == 'water': self.color = c.BLUE
		elif self.status == 'abyss': self.color = c.BLACK