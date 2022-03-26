from cgi import test
from hmac import new
import main as turtlegui
testElement = turtlegui.Element()

def test(element):
    print(element)

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

#testElement = turtlegui.Element()
#testElement.setx(500)
#testElement.sety(500)
#testElement.setwidth(200)
#testElement.setheight(200)
#testElement.setcolor("32a852")
#testElement.setcontent("Hello World!")
#testElement.render()

testElement.finish()