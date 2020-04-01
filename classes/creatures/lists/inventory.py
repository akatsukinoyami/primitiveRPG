from classes.creatures.lists.items import Items

class Inventory:
	def __init__(self):
		items = Items()
		self.head       = items.init_cap
		self.right_hand = items.init_sword
		self.left_hand  = items.init_sheild
		self.cheast     = items.init_brp
		self.pants      = items.init_pants
		self.boots      = items.init_boots
		self.backpack   = []