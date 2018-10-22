from fltk import *
import random
import glob
from time import sleep

sqside = 200
win = Fl_Window(Fl_w()/2-2*sqside,Fl_h()/2-(4*sqside+40),4*sqside,5*sqside)
grid = []
imgs = []
chosen = []
imgfiles = {}

def clicked(widg):
    global chosen
    global win
    if Fl.event_button() == FL_LEFT_MOUSE:
        # Only select new if not duplicate square
        if len(chosen) <= 1 and widg not in chosen:
            chosen.append(widg)
            widg.color(FL_DARK_YELLOW)
        elif len(chosen) == 2:
            print len(chosen)

    elif Fl.event_button() == FL_RIGHT_MOUSE:
        if widg in chosen:
            widg.color(FL_GRAY)
            chosen.remove(widg)

def reshift(widg):
    global imgs
    global chosen
    for sq in chosen:
        sq.image(imgs[grid.index(sq)].copy(sqside,sqside))
        sq.redraw()
#    print imgfiles[(imgs[grid.index(chosen[0])])], imgfiles[(imgs[grid.index(chosen[1])])]
#    print imgfiles[(imgs[grid.index(chosen[0])])]==imgfiles[(imgs[grid.index(chosen[1])])]
    sleep(2)
    if imgfiles[(imgs[grid.index(chosen[0])])] == imgfiles[(imgs[grid.index(chosen[1])])]:
        for sq in chosen:
            sq.deactivate()
    else:
        for sqb in grid:
            sqb.deactivate()
            if sqb in chosen:
                sqb.image(None)

for file in glob.glob("./imgs/*"):
    for rep in range(2):
        img = Fl_JPEG_Image(file)
        imgs.append(img)
        imgfiles[img] = file
print imgfiles

#random.shuffle(imgs)

win.begin()
for row in range(4):
    for column in range(4):
        grid.append(Fl_Button(row*sqside,column*sqside,sqside,sqside))
        grid[-1].callback(clicked)

showbut = Fl_Button(sqside*2-160/2,sqside*4+40,160,40,'SHOW')
win.end()

showbut.callback(reshift)

win.show()
Fl.run()
