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
testElement.setfontsize(16)
testElement.onclick(test)
testElement.render()

tkgui.finish()

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

