from classes.tech.colors 	import Colors

class Map:
	def __init__(self, surf, rect):
		self.surf, self.rect = surf, rect
		
	def draw_grid(self, g, line, world):
		m = world.map
		for row in m:
			for c in row:
				x = c.x*c.size
				y = c.y*c.size
				g.draw.rect(self.surf, c.color,	(x, y, c.size, c.size))
				g.draw.rect(self.surf, line,	(x, y, c.size, c.size), 2)
		
		c = Colors()
		h = world.hero
		g.draw.rect(self.surf, c.PINK, (h.x-9, h.y-9, 20, 20))
		
		
		

				


