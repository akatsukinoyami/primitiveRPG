class Info:
	def __init__(self, surf, rect):
		self.surf, self.rect = surf, rect 

	def draw_grid(self, g, line, world=0):
		g.draw.rect(self.surf, line, (0, 0, self.rect.width, self.rect.height), 2)
