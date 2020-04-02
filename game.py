from classes.tech.colors		import Colors
from classes.windows.window		import Window
from classes.locations.world	import World
import pygame as g

g.init()

def main():
	FPS 	= 60
	WINDOW 	= (1024, 1024)

	display = g.display.set_mode(WINDOW)
	clock	= g.time.Clock()

	w		= World('katsu')
	wd		= Window(g, WINDOW)

	while True:
		w.hero.world = w
		for i in g.event.get():
			if 	 i.type == g.QUIT: exit()
			elif i.type == g.KEYDOWN:
				w.hero.move(g, wd, i)
		
		s, r = wd.surface(g, w)
		display.blit(s, r)
		
		g.display.update()
		clock.tick(FPS)

if __name__ == "__main__": 
	main()