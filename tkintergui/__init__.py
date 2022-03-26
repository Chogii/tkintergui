#from tkinter.tix import Tk
#from tkinter.tix import Tk
import turtle as t
import tkinter as tk
#from tkinter import Tk, tix
win =  tk.Tk()
win.withdraw()
scxscale = 0.6
scyscale = 0.6
screen = t.Screen()
screen.setup(scxscale,scyscale)
t.penup()
t.ht()
t.speed('fastest')
global cur
cur = None
global elements
elements = []

def placeholder(element):
  None

def valColor(color):
  if(len(color) == 6):
    for _,i in enumerate(color.lower()):
      our = ord(i)
      if(our < 48 or our > 102):
        return 1
        break
  else:
    return 1

class Element:
  """
  Create a basic element which you can assign many
  different attributes to such as color, size,
  position, content and onclick procedures
  """
  def render(self):
    """
    Render the element onto the screen. This must be ran every time you want to push a visual change through
    """
    if(self.hidden == False):
      self.turtle.pu()
      self.turtle.turtlesize(self.width / 20.2, self.height / 20.2, 0)
      self.turtle.goto((win.winfo_screenwidth() * scxscale / 2 * -1) + self.x + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * scyscale / 2) - self.y - self.height + (self.height / 2 - 2))
      self.wturtle.clear()
      self.wturtle.color("#" + self.textcolor)
      self.wturtle.goto((win.winfo_screenwidth() * scxscale / 2 * -1) + self.x + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * scyscale / 2) - self.y - self.height + (self.height / 2 - 2) - self.fontsize * 0.8)
      self.wturtle.write(self.content,True,"Center",[self.fontfamily,self.fontsize,self.fonttype])
  
  def __init__(self):
    self.turtle = t.Turtle()
    self.turtle.speed('fastest')
    self.turtle.seth(270)
    self.turtle.shape("square")
    self.turtle.pu()

    self.wturtle = t.Turtle()
    self.wturtle.ht()
    self.wturtle.speed('fastest')
    self.wturtle.seth(270)
    self.wturtle.shape("square")
    self.wturtle.pu()

    self.x = 0
    self.y = 0
    self.onclickfunc = placeholder
    self.width = 0
    self.height = 0
    self.color = "000000"
    self.textcolor = "000000"
    self.fontfamily = "Sans Serif"
    self.fontsize = 16
    self.fonttype = 'normal'
    self.content = ''
    self.hidden = False

    elements.append(self)

  def hide(self):
    self.hidden = True
    self.turtle.ht()
    self.turtle.goto(-1000,-1000)
    self.wturtle.clear()

  def show(self):
    if(self.hidden == True):
      self.hidden = False
      self.turtle.st()
      self.render()

  def setx(self,xgiven: int):
    """
    Set the x-coordinate location of the element in pixels. every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.x = xgiven

  def sety(self,ygiven: int):
    """
    Set the y-coordinate location of the element in pixels. every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.y = ygiven

  def setwidth(self,xgiven: int):
    """
    Set the visual width of the element in pixels
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.width = xgiven

  def setheight(self,ygiven: int):
    """
    Set the visual height of the element in pixels
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.height= ygiven

  def setcolor(self,colorgiven: str):
    """
    Set the color of the element in a hexadecimal color code. Examples:\n
    'FF0000'\n
    'ccee99'\n
    '000011'\n
    """
    if not isinstance(colorgiven,str):
      raise TypeError("color must be a string in hexadecimal color code")
    if(valColor(colorgiven) != 1):
      self.color = colorgiven
      self.turtle.color("#" + colorgiven)
    else:
      raise Exception("color was not accepted. color must be a hexadecimal color code")

  def settextcolor(self,colorgiven: str):
    """
    Set the color of the element's text content in a hexadecimal color code. Examples:\n
    'FF0000'\n
    'ccee99'\n
    '000011'\n
    """
    if not isinstance(colorgiven,str):
      raise TypeError("color must be a string in hexadecimal color code")
    if(valColor(colorgiven) != 1):
      self.textcolor = colorgiven
    else:
      raise Exception("color was not accepted. color must be a hexadecimal color code")

  def setfontfamily(self,familygiven: str):
    """
    Set the font family of the element's text content by the font's name
    """
    if not isinstance(familygiven,str):
      raise TypeError("family must be a string")
    self.fontfamily = familygiven

  def setfontsize(self,sizegiven: int):
    """
    Set the font size of the element's text content
    """
    if not isinstance(sizegiven,int):
      raise TypeError("family must be an integer")
    self.fontsize = sizegiven

  def setcontent(self,contentgiven: str):
    """
    Set the element's text content
    """
    if not isinstance(contentgiven,str):
      raise TypeError("content must be a string")
    self.content = str(contentgiven)

  def onclick(self,func):
    """
    Set the function you want to be called when the element is clicked on. The first argument will always be the element that was clicked. Pass 'disable' instead of a function if you want to disable this after setting it already
    """
    if(callable(func)):
      self.onclickfunc = func
    elif(func == "disable"):
      self.onclickfunc = placeholder
    else:
      raise TypeError("argument must be a function")

  #def renderold(self):
  #  if(self.rendered == False):
  #    self.rendered = True
  #    t.setx(self.x)
  #    t.sety(self.y)
  #    t.color("#" + self.color)
  #    t.seth(0)
  #    t.pendown()
  #    t.begin_fill()
  #    for i in range(2):
  #      t.forward(self.width)
  #      t.left(90)
  #      t.forward(self.height)
  #      t.left(90)
  #    t.end_fill()
  #    t.penup()
  
  def finish(self):
    t.done()
    
def click(data):
  for _,element in enumerate(elements):
    if(data.x in range(element.x,element.x + element.width) and data.y in range(element.y,element.y + element.height)):
      element.onclickfunc(element)

    
#t.onscreenclick(click)
ws = t.getcanvas()
ws.bind('<Button-1>',click)

def pause():
  if True:
    t.ontimer(pause,250)