from fltk import *
import random

sqside = 200
win = Fl_Window(Fl_w()/2-2*sqside,Fl_h()/2-(4*sqside+40),4*sqside,5*sqside)
grid = []

win.begin()
for row in range(4):
	for column in range(4):
		grid.append(Fl_Button(row*sqside,column*sqside,sqside,sqside))

showbut = Fl_Button(sqside*2-160/2,sqside*4+40,160,40)
win.end()

win.show()
Fl.run()
