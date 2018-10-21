from fltk import *
import random
import glob

sqside = 200
win = Fl_Window(Fl_w()/2-2*sqside,Fl_h()/2-(4*sqside+40),4*sqside,5*sqside)
grid = []
imgs = []
chosen = []
selec = 0

def clicked(widg, pos):
	global imgs
	global selec
	if Fl.event_button() == FL_LEFT_MOUSE:
		if selec <= 1:
			widg.image(imgs[pos].copy(sqside,sqside))
			chosen.append(widg)
			selec += 1
		elif selec == 2:
#			print selec
			#TODO: compare actual image files, not instances of Fl_JPEG_Image
			print (imgs[grid.index(chosen[0])]).data
			print (imgs[grid.index(chosen[1])]).data
			if (imgs[grid.index(chosen[0])]).data == (imgs[grid.index(chosen[1])]).data:
				for sq in chosen:
					sq.deactivate()

	elif Fl.event_button() == FL_RIGHT_MOUSE:
		widg.image(None)
		selec -= 1
		
def reshift(widg):
	global selec
	selec = 0

for file in glob.glob("./imgs/*"):
	for rep in range(2):
		imgs.append(Fl_JPEG_Image(file))
random.shuffle(imgs)

win.begin()
for row in range(4):
	for column in range(4):
		grid.append(Fl_Button(row*sqside,column*sqside,sqside,sqside))
		grid[-1].callback(clicked,(row*4+column))

showbut = Fl_Button(sqside*2-160/2,sqside*4+40,160,40,'SHOW')
win.end()

showbut.callback(reshift)

win.show()
Fl.run()
