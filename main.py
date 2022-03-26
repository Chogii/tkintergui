from tkinter.tix import Tk
import turtle as t
import tkinter as tk
win = Tk()
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

def placeholder():
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
  def render(self):
    self.turtle.pu()
    self.turtle.turtlesize(self.width / 20.2, self.height / 20.2, 0)
    self.turtle.goto((win.winfo_screenwidth() * scxscale / 2 * -1) + self.x + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * scyscale / 2) - self.y - self.height + (self.height / 2 - 2))
    t.color("#" + self.textcolor)
    t.goto((win.winfo_screenwidth() * scxscale / 2 * -1) + self.x + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * scyscale / 2) - self.y - self.height + (self.height / 2 - 2) - self.fontsize * 0.8)
    t.write(self.content,True,"Center",[self.fontfamily,self.fontsize,self.fonttype])
  
  def __init__(self):
    self.turtle = t.Turtle()
    self.turtle.speed('fastest')
    self.turtle.seth(270)
    self.turtle.shape("square")
    self.turtle.pu()

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

    elements.append(self)

  def setx(self,xgiven):
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.x = xgiven

  def sety(self,ygiven):
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.y = ygiven

  def setwidth(self,xgiven):
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.width = xgiven

  def setheight(self,ygiven):
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.height= ygiven

  def setcolor(self,colorgiven):
    if not isinstance(colorgiven,str):
      raise TypeError("color must be a string in hexadecimal color code")
    if(valColor(colorgiven) != 1):
      self.color = colorgiven
      self.turtle.color("#" + colorgiven)

  def settextcolor(self,colorgiven):
    if not isinstance(colorgiven,str):
      raise TypeError("color must be a string in hexadecimal color code")
    if(valColor(colorgiven) != 1):
      self.textcolor = colorgiven

  def setfontfamily(self,familygiven):
    if not isinstance(familygiven,str):
      raise TypeError("family must be a string")
    self.fontfamily = familygiven

  def setfontsize(self,sizegiven):
    if not isinstance(sizegiven,int):
      raise TypeError("family must be an integer")
    self.fontsize = sizegiven

  def setcontent(self,contentgiven):
    if not isinstance(contentgiven,str):
      raise TypeError("content must be a string")
    self.content = str(contentgiven)

  def onclick(self,func):
    if(callable(func)):
      self.onclick = func
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