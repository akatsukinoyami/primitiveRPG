from classes.tech.colors		import Colors
from classes.windows.window		import Window
from classes.locations.world	import World
import pygame as g

g.init()

def main():
	FPS 	= 60
	WINDOW 	= (800, 600)

	display = g.display.set_mode(WINDOW)
	clock	= g.time.Clock()

	w		= World('katsu')
	wd		= Window(g, WINDOW)
	w 		= wd.init_world(w)

	while True:
		for i in g.event.get():
			if 	 i.type == g.QUIT: exit()
			elif i.type == g.KEYDOWN:
				if 	 i.key == g.K_RIGHT:w.hero.move(   1)
				elif i.key == g.K_UP:	w.hero.move( 0.5)
				elif i.key == g.K_LEFT: w.hero.move(  -1)
				elif i.key == g.K_DOWN: w.hero.move(-0.5)
		
		s, r = wd.surface(g, w)
		display.blit(s, r)
		
		g.display.update()
		clock.tick(FPS)

if __name__ == "__main__": 
	main()