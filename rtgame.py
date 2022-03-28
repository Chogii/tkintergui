from bisect import bisect_right
import tkintergui as gui
import time
import datetime
import random

infobox = gui.Element()
reactbox = gui.Element()
global state
global taken
global start
state = 0
taken = [0,0]

def results():
    global state
    global taken
    if(state == 1):
        reactbox.setcontent("Too early! Click to start again")
        state = 0
    elif(state == 2):
        state = 0
        taken[1] = time.time()
        reactbox.setcontent(str( round( ((taken[1] - taken[0]) * 1000 ),2)) + "ms. Click to start again" )
    reactbox.render()
    state = 0

def activate(object):
    global state
    global taken
    if state == 0:
        state = 1
        infobox.setcontent("When the square turns green, click!")
        infobox.render()
        reactbox.setcolor("FF0000")
        reactbox.setcontent("Wait...")
        reactbox.render()
        #time.sleep(random.randrange(2,5))
        for i in range(random.randrange(20,50)):
            time.sleep(0.1)
            if(state != 1):
                break
        if(state == 1):
            state = 2
            reactbox.setcolor("00FF00")
            reactbox.setcontent("Now!")
            taken[0] = time.time()
            reactbox.render()
    else:
        results()


infobox.setcontent("When the square turns green, click!")
infobox.settextcolor("000000")
infobox.setcolor("FFFFFF")
infobox.setheightpercent(10)
infobox.setwidthpercent(50)
infobox.setypercent(20)
infobox.setxpercent(50)
infobox.render()

reactbox.setcontent("Click to start")
reactbox.settextcolor("FFFFFF")
reactbox.setcolor("035afc")
reactbox.setheightpercent(20)
reactbox.setwidthpercent(40)
reactbox.setypercent(40)
reactbox.setxpercent(50)
reactbox.setfontsize(25)
reactbox.onclick(activate)
reactbox.render()

gui.finish()