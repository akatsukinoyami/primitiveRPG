from random import randint
from classes.tech.colors import Colors as c

class Somebody: #to love
	def __init__(self, 
		world, name,
		x=16, y=16,
		color=c.PINK,
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

		self.world		= world
		self.name       = name

		self.x, self.y	= x, y
		self.color		= color
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

	def draw(self, draw, surface):
		draw.rect(surface, self.color, (self.x-9, self.y-9, 20, 20))
		return surface
	
	def move(self, g, wd, i):
		cS = self.world.cell_size*3
		mw = wd.map.rect.width
		mh = wd.map.rect.height
		camera = self.world.camera
		x, y = 0,0
		if   i.key == g.K_LEFT:	
			if self.x <= cS:	self.world.camera = (camera[0]-1, 	camera[1])
			else:				x =-32
		elif i.key == g.K_RIGHT:	
			if self.x >= mw-cS:	self.world.camera = (camera[0]+1, 	camera[1])
			else:				x = 32
		elif i.key == g.K_UP:		
			if self.y <= cS:	self.world.camera = (camera[0], 	camera[1]-1)
			else:				y =-32
		elif i.key == g.K_DOWN:	
			if self.y >= mh-cS:	self.world.camera = (camera[0], 	camera[1]+1)
			else:				y = 32
	
		
		z = self.world.height_generator((self.x+x)//self.world.cell_size,
										(self.y+y)//self.world.cell_size)
		
		if z != 2 and z != -2:
			self.x+=x
			self.y+=y
		else:
			self.world.camera = camera
		