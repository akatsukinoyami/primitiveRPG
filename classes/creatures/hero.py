from classes.creatures.creature     	import Somebody
from classes.creatures.lists.inventory	import Inventory
from classes.tech.colors 				import Colors
c = Colors()

class Hero(Somebody):
	def __init__(self, name):
		super().__init__(name, x=16, y=16)
		self.exp        = 1
		self.level      = 1
		self.money      = 100
		self.inventory  = Inventory()
	
	def move(self, d):
		if   d ==    1: self.x+=32
		elif d ==   -1: self.x-=32
		elif d ==  0.5: self.y-=32
		elif d == -0.5: self.y+=32
	