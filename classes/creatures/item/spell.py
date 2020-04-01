class Spell:
    def __init__(self, 
				abbr, name, descr,
                attack	=0, 
				def_act	=0, 
				heal	=0, 
				restam	=0, 
				cost	=0):
        
        self.abbr    = abbr
        self.name    = name 
        self.descr   = descr

        self.attack  = attack
        self.def_act = def_act

        self.heal    = heal
        self.restam  = restam

        self.cost    = cost
        
    def heal_f(self, user):
        user.health += self.heal
    
    def restam_f(self, user):
        user.stamina += self.restam
    
    def take_sacrifice(self, user):
        user.mana -= self.cost