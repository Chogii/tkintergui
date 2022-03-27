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
import tkintergui as turtlegui

testElement = turtlegui.Element()

def test(element):
    element.hide()
    element.setx(300)
    element.sety(300)
    element.setcontent(element.data)
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
testElement.setdata("I'm Here Now!")
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

testElement.finish()

# This example literally shows the full capabilities of this module so far
```

## The 'finish' method

You must use the 'finish' method at the end of your code or your program will exit on its own

```py
import tkintergui as tkgui

element = tkgui.Element()
element.setx(50)
element.sety(50)
element.setwidth(100)
element.setheight(100)

tkgui.finish()
```

## Classes

### 'Element'

An element is a rectangle that can be any color, contain text, be anywhere on the screen with any size, and perform functions for you when they are clicked

```py
import tkintergui as tkgui

element = tkgui.Element()
```
**Methods**

**setx(*int*)**

Set the position of the element on the x-coordinate plane in pixels

```py
testElement.setx(100)
```

**sety(*int*)**

Set the position of the element on the y-coordinate plane in pixels

```py
testElement.sety(150)
```

**setwidth(*int*)**

Set the width of the element in pixels 

```py
testElement.setwidth(200)
```

**setheight(*int*)**

Set the height of the element in pixels 

```py
testElement.setheight(50)
```

**setcolor(*(Hexadecimal Color Code)*)**

Set the color of the element with a hexadecimal color code

```py
testElement.setcolor('FF00CC')
```

**setcontent(*str*)**

Set the text the element contains. Text always appear at the center of an element

```py
testElement.setcontent("Hello World!")
```

**settextcolor(*(Hexadecimal Color Code)*)**

Set the text color of the element's content with a hexadecimal color code

```py
testElement.setcolor('00FFEE')
```

**setfontfamily(*str*)**

Set the font family of the element's content with the name of the font

```py
testElement.setfontfamily('Sans Serif')
```

**setfontsize(*int*)**

Set the font size of the element's content

```py
testElement.setfontsize(16)
```

**setdata(*any*)**

Assign any data you want to an element which you can retrieve later with ``element.data``

```py
testElement.setdata("Hello World!")
print(testElement.data) 
# >> "Hello World!"
```

**hide()**

Hides the element from view and makes it intangible until shown again. This method does not require ``render()`` in order to be pushed

```py
testElement.hide()
```

**show()**

Shows the element after being hidden. This method does not require ``render()`` in order to be pushed

```py
testElement.show()
```

**render()**

Render an element. You must do this every time you want to push a visual change; Any methods from before will not visually update the element on its own

```py
testElement.render()
```

**Variables**

**turtle** (turtle object)

The turtle variables contains the turtle object which is literally the element itself. Any methods from the original turtle module can be applied to this one, but is generally not recommended!

**wturtle** (turtle object)

Another turtle object within the element but is only responsible for rendering text

**x** (int)

The x position of the element on the screen

**y** (int)

The y position of the element on the screen

**onclickfunc** (fun)

The function the element will perform whenever it is clicked

**width** (int)

The width of the element's size

**height** (int)

The height of the element's size

**color** (str)

The hexadecimal color of the element

**content** (str)

The text content the element will render at its center

**textcolor** (str)

The hexadecimal color of the element's rendered text content 

**fontfamily** (str)

The name of the font family the text content will be rendered in

**fontsize** (int)

The size the text content will be rendered in

**hidden** (bool)

Identifies whether or not the element is hidden from view at the moment



