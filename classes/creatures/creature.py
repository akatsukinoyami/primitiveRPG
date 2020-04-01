from random import randint

class Somebody: #to love
	def __init__(self, 
		name,
		x=16, y=16,
		health  = 100, 
		stamina = 100, 
		mana    = 100,
		attack  = 1,   
		def_pass= 1,   
		def_act = 10,  
		agility = 1, 
		intel	= 1,
		skills	= [], 
		spells	= [], 
		mode = 'normal'): #'defend', 'wait', 'stunned'

		self.name       = name
		self.x, self.y	= x, y
		self.health     = health
		self.stamina    = stamina
		self.mana       = mana
		self.attack     = attack
		self.def_pass   = def_pass
		self.def_act    = def_act
		self.agility    = agility
		self.intel      = intel
		self.skills     = skills
		self.mag_book   = spells
		self.mode       = mode 

	def attack_f(self, enemy, damage):
		act, damage = enemy.get_damage(enemy, self.attack)
		return act, enemy.health, damage
	
	def defend_f(self, enemy, damage): 
		self.mode = 'defend'
		return self.mode

	def wait_f(self, enemy, damage):   
		self.mode = 'wait'
		return self.mode

	def get_damage(self, damage):
		end_damage = damage
		if self.mode == 'normal':
			if self.agility >= randint(0, 100): return 'avoided', 0
			end_damage -= self.def_pass

		elif self.mode == 'defend': end_damage -= self.def_act
		elif self.mode == 'wait':   pass

		self.health -= end_damage
		self.mode = 'normal'
		return 'damaged', end_damage
		
	@staticmethod
	def draw(draw, surface, color, x, y):
		return draw.rect(surface, color, (x, y, 20, 20), 5)