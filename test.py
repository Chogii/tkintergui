from cgi import test
import main as turtlegui

testElement = turtlegui.Element()
testElement.setx(100)
testElement.sety(50)
testElement.setwidth(200)
testElement.setheight(50)
testElement.setcolor("32a852")
testElement.setcontent("Hello World!")
testElement.render()

testElement = turtlegui.Element()
testElement.setx(-100)
testElement.sety(-50)
testElement.setwidth(50)
testElement.setheight(200)
testElement.setcolor("32a852")
testElement.setcontent("Hello World!")
testElement.render()

testElement.finish()