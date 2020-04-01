from classes.creatures.hero	import Hero
from classes.locations.cell import Cell

class World:
	def __init__(self, name):
		self.hero = Hero(name)
		self.map = []
	
	def init_map(self, r):
		cell = 32
		for x in range(r.width//cell):
			row = []
			for y in range(r.height//cell):
				row.append(Cell(x, y, cell))
			self.map.append(row)