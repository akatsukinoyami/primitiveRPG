from classes.creatures.creature     	import Somebody
from classes.creatures.lists.inventory	import Inventory
from classes.tech.colors 				import Colors
c = Colors()

class Hero(Somebody):
	def __init__(self, world, name):
		super().__init__(world, name, x=16, y=16)
		self.exp        = 1
		self.level      = 1
		self.money      = 100
		self.inventory  = Inventory()
		self.world		= world
	