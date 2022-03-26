# tkintergui
Tkinter GUI is a Python GUI viewer with support for buttons and button events using tkinter and turtle.

## Getting Started

To get started, save the 'tkintergui' folder anywhere on your computer and import it properly

```
project
│   test.py  
│
└───tkintergui
    | ...
```

```py
# test.py
import tkintergui as tkgui

testElement = tkgui.Element()

def test(element):
    element.setcontent('Good Job!')
    element.render()
    print("Hello World!")
    element.onclick('disable')

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

# This example literally shows the full capabilities of this module so far
```

## Classes

### Elements

An element can be any color, contain text, be anywhere on the screen with any size, and perform functions for you when they are clicked

```py
import tkintergui as tkgui

testElement = tkgui.Element()
```
**Methods**

**setx(*int*)**

Set the 
