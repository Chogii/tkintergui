from cgi import test
from hmac import new
import main as turtlegui
testElement = turtlegui.Element()

def test(element):
    element.setcontent('Good Job!')
    element.render()
    print("Hello World!")
    element.onclick('disable')

def test2(element):
    print("hello world")

testElement.setx(100)
testElement.sety(100)
testElement.setwidth(200)
testElement.setheight(50)
testElement.setcolor("5069E5")
testElement.setcontent("Button")
testElement.settextcolor("FFFFFF")
testElement.setfontfamily("Segoe UI")
testElement.onclick(test)
testElement.render()

testElement2 = turtlegui.Element()

testElement2.setx(200)
testElement2.sety(200)
testElement2.setwidth(200)
testElement2.setheight(100)
testElement2.setcolor("FF0000")
testElement2.setcontent("Button")
testElement2.settextcolor("FFFFFF")
testElement2.setfontfamily("Segoe UI")
testElement2.render()

testElement.render()
testElement.finish()