from classes.creatures.item.item import Item

class Items:
	#head
	init_cap		= Item('head', 		'init_cap', 	'Кепка',	'Простая кепка', 	def_pass=1)
	#right_hand
	init_sword		= Item('right_hand','init_sword', 	'Меч',  	'Ржавый меч',  		attack=3)
	#left_hand
	init_sheild		= Item('left_hand', 'init_sheild', 	'Щит',  	'Прохудившийся щит',def_act=1)
	#cheast
	init_brp		= Item('cheast',	'init_brp',		'Кольчуга',	'Ржавая кольчуга',	def_pass=1)
	#pants
	init_pants		= Item('pants', 	'init_pants', 	'Штаны',   	'Просто штаны')
	#boots
	init_boots		= Item('boots', 	'init_boots', 	'Ботинки', 	'Старые ботинки', 	agility=1)