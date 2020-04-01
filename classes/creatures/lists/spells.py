from classes.creatures.item.spell import Spell

class Spells:
	fireball	= Spell('fireball', 'Файербол',      'Просто огненный шар',  attack=5, cost=10)
	heal   		= Spell('heal_sm',  'Лечение малое', 'Лечит небольшие раны', heal=5,   cost=7)
