from cgi import test
from hmac import new
import tkintergui as turtlegui

testElement = turtlegui.Element()

def test(element):
    element.hide()
    element.setx(300)
    element.sety(300)
    element.setcontent("I'm here now!")
    element.render()
    element.onclick('disable')

testElement.setx(100)
testElement.sety(100)
testElement.setwidth(200)
testElement.setheight(50)
testElement.setcolor("5069E5")
testElement.setcontent("Button")
testElement.settextcolor("00FF00")
testElement.setfontfamily("Segoe UI")
testElement.onclick(test)
testElement.render()

def test2(element):
    testElement.show()

testElement2 = turtlegui.Element()

testElement2.setx(200)
testElement2.sety(200)
testElement2.setwidth(200)
testElement2.setheight(100)
testElement2.setcolor("FF0000")
testElement2.setcontent("Button")
testElement2.settextcolor("FFFFFF")
testElement2.setfontfamily("Segoe UI")
testElement2.onclick(test2)
testElement2.render()

turtlegui.finish()