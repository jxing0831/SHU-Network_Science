from pylab import *
from six.moves import xrange
import module as md
truck=md.Car()
truck.printname()
def initialize(x0, y0): ###
    global x, y, xresult, yresult
    x = x0 ###
    y = y0 ###
    xresult = [x]
    yresult = [y]

def observe():
    global x, y, xresult, yresult
    xresult.append(x)
    yresult.append(y)

def update():
    global x, y, xresult, yresult
    nextx = 0.5 * x + y
    nexty = -0.5 * x + y
    x, y = nextx, nexty

for x0 in arange(-2, 2, .5): ###
    for y0 in arange(-2, 2, .5): ###
        initialize(x0, y0) ###
        for t in xrange(30):
            update()
            observe()
        plot(xresult, yresult, 'b') ###

show()



