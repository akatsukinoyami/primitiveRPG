from classes.creatures.hero	import Hero
from random					import randint
from opensimplex 			import OpenSimplex


class World:
	def __init__(self, name):
		self.hero	= Hero(self, name)
		self.battle	= False
		self.cell_size=32
		self.camera = (0,0)
		self.seed   = randint(0,10000)
		self.noise  = OpenSimplex(self.seed)
	
	def height_generator(self, x, y):
		z = int(
				self.noise.noise2d(
					(x+self.camera[0])/9, 
					(y+self.camera[1])/9
					)
				*4)
		if   z == 3 or z == 4: z = 2
		elif z ==-3 or z ==-4: z =-2
		return z