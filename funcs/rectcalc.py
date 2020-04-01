def calc(g, win, x, y, W, H):
	t = lambda a, b: a*b/100
	r = g.Rect( t(win[0], x), t(win[1], y), 
				t(win[0], W), t(win[1], H))
	s = g.Surface((r.width, r.height))
	return s, r