from classes.tech.colors 	import Colors

class Map:
	def __init__(self, surf, rect):
		self.surf, self.rect = surf, rect
		
	def draw_grid(self, g, line, world):
		c = Colors()
		s = world.cell_size

		for x in range(self.rect.width//s):
			for y in range(self.rect.height//s):
				heights = {	2:c.WHITE, 1:c.GRAY, 
							0:c.GREEN, 
							-1:c.YELLOW, -2:c.BLUE}
				z = world.height_generator(x, y)
				g.draw.rect(self.surf, heights[z], 	(x*s, y*s, s, s))
				g.draw.rect(self.surf, line,		(x*s, y*s, s, s), 2)
				
		self.surf = world.hero.draw(g.draw, self.surf)
		g.draw.rect(self.surf, line, (0, 0, self.rect.width, self.rect.height), 1)