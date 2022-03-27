import tkintergui as gui

dummy = gui.Element()

dummy.setwidthpercent(20)
dummy.setheightpercent(20)
dummy.setcolor("FF0000")
dummy.setxpercent(50)
dummy.setypercent(50)
dummy.setcontent("Hello World!")
dummy.settextcolor("000000")
dummy.render()

gui.finish()