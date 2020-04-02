from funcs.rectcalc			import calc
from classes.windows.map	import Map
from classes.windows.dialog import Dialog
from classes.windows.stat	import Stats
from classes.windows.info	import Info
from classes.tech.colors 	import Colors
c = Colors()

class Window:
	def __init__(self, g, win):
		#позволяет подать в Rect проценты от размера окна
		self.surf, self.rect = calc(g, win,  0,  0, 100, 100)
		msurf, mrect = calc(g, win,  0,  0,  80,  80)
		dsurf, drect = calc(g, win,  0, 80,  80,  20)
		ssurf, srect = calc(g, win, 80,  0,  20, 50)
		isurf, irect = calc(g, win, 80, 50,  20, 50)

		self.map 	 = Map(	  msurf, mrect)
		self.dialog	 = Dialog(dsurf, drect)
		self.stats	 = Stats( ssurf, srect)
		self.info	 = Info(  isurf, irect)

	def surface(self, g, world):
		for i in (self.map, self.dialog, self.info, self.stats):
			i.surf.fill(c.BLACK)
			i.draw_grid(g, c.DARK_GRAY, world)
			self.surf.blit(i.surf, i.rect)

		return self.surf, self.rect