from classes.creatures.creature import Somebody

class Enemies:
    def __init__(self):
        self.zhaba 	= Somebody('Жаба',  
					health  = 20, attack  = 1,  intel   = 1,
					stamina = 20, def_pass= 1,  def_act = 10,
					mana    = 20, agility = 10, mode    = 'normal')
        
        self.bandit = Somebody('Бандит',
					health  = 20, attack  = 1, intel   = 1,
					stamina = 20, def_pass= 1, def_act = 10,
					mana    = 20, agility = 1, mode    = 'normal')