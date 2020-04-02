import pygame as g
from random 		import randint, choice, random
from opensimplex 	import OpenSimplex
g.init()

def main():

	FPS 	= 1
	WINDOW 	= (1000, 1000)

	
	display = g.display.set_mode(WINDOW)
	clock	= g.time.Clock()
	size,seed= 10, 1
	q 		= 1

	while True:
		display.fill((0,0,0))
		for i in g.event.get():
			if 	 i.type == g.QUIT: exit()
			elif i.type == g.KEYDOWN:
				if 	 i.key == g.K_RIGHT:size+=5
				elif i.key == g.K_LEFT: size-=5
				elif i.key == g.K_UP:	q+=1
				elif i.key == g.K_DOWN: q-=1
				if size == 0: size = 4
		
		seed+=1
		noise = OpenSimplex(seed=seed)
		for x in range(WINDOW[0]//size):
			for y in range(WINDOW[1]//size):
				s1 = noise.noise2d(x/q, y/q)
				s = int(s1*3)
				t = {	 2 : (  0,   0,   0),
						 1 : (255, 255, 255),
						 0 : (  0, 200,  64),
						-1 : (225, 225,   0),
						-2 : (  0,   0, 225),}
				g.draw.rect(display, t[s], (x*size, y*size, size, size))
		g.display.update()
		
		clock.tick(FPS)

if __name__ == "__main__": 
	main()