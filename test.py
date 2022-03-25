from cgi import test
import main as turtlegui

testElement = turtlegui.Element()
testElement.setx(100)
testElement.sety(0)
testElement.setwidth(200)
testElement.setheight(50)
testElement.setcolor("32a852")
testElement.setcontent("Hello World!")
testElement.render()