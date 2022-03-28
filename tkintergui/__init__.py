#from tkinter.tix import Tk
#from tkinter.tix import Tk
import turtle as t
import tkinter as tk
from tkinter import messagebox as msg
import time
from typing import Type
import platform
#from tkinter import Tk, tix
win =  tk.Tk()
win.withdraw()
#scxscale = 0.6
#scyscale = 0.6
screen = t.Screen()
canvas = screen.getcanvas()
t.penup()
t.ht()
t.speed('fastest')
t.tracer(True,0)
global cur
cur = None
global elements
elements = []
global userconfig
userconfig = {
  "RESIZABLE":False,
  "SCREEN_SIZE_METHOD":0,
  "SCREEN_SIZE":[0.6,0.6],
  "FULLSCREEN":True,
  "TITLE":"Made with TkinterGUI",
  "WINDOWS_DISABLED":False,
  "MAC_DISABLED":False,
  "LINUX_DISABLED":False
}
availmethods = [0,1]


def setresizable(toggle: bool):
  """
  Set whether or not the window can be risized by the user
  """
  if type(toggle) != bool:
    raise TypeError("setresizable only accepts a boolean 'True' or 'False'")
  else:
    userconfig["RESIZABLE"] = toggle

def setscreensizemethod(method: int):
  """
  Set the resizing method for the screen. Available methods are:
  0: Defined by percentage (0 to 100)
  1: Defined by pixels (positive integer)
  """
  if type(method != int):
    raise TypeError("setscreensizemethod only accepts an integer")
  else:
    if method in range(0,len(availmethods)):
      userconfig["SCREEN_SIZE_METHOD"] = method
    else:
      raise Exception("defined method " + str(method) + " does not exist")

def setscreensize(x: int,y: int):
  if type(x) != int or type(y) != int:
    raise TypeError("both x and y arguments must be an integer value")
  if x < 0 or y < 0:
    raise Exception("both x and y values must be a positive integer")
  if(userconfig["SCREEN_SIZE_METHOD"] == 1):
    x = x / win.winfo_screenwidth
    y = y / win.winfo_screenheight
  else:
    x = x / 100
    y = y / 100
  userconfig["SCREEN_SIZE"] = [x,y]

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
      self.turtle.showturtle()
      self.turtle.turtlesize((self.width + self.widthper[0]) / 20.2, (self.height + self.heightper[0]) / 20.2, 0)
      self.turtle.goto((win.winfo_screenwidth() * userconfig["SCREEN_SIZE"][0] / 2 * -1) + self.x + self.xper[0] + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * userconfig["SCREEN_SIZE"][1] / 2) - self.y - self.yper[0] - self.height + (self.height / 2 - 2))
      self.wturtle.clear()
      self.wturtle.color("#" + self.textcolor)
      self.wturtle.goto((win.winfo_screenwidth() * userconfig["SCREEN_SIZE"][0] / 2 * -1) + self.x + self.xper[0] + self.width - (self.width / 2 - 2), (win.winfo_screenheight() * userconfig["SCREEN_SIZE"][1] / 2) - self.y - self.yper[0] - self.height + (self.height / 2 - 2) - self.fontsize * 0.8)
      self.wturtle.write(self.content,True,"Center",[self.fontfamily,self.fontsize,self.fonttype])
  
  def __init__(self):
    self.wturtle = t.Turtle()
    self.wturtle.ht()
    self.wturtle.speed('fastest')
    self.wturtle.seth(270)
    self.wturtle.shape("square")
    self.wturtle.pu()

    self.turtle = t.Turtle()
    self.turtle.ht()
    self.turtle.speed('fastest')
    self.turtle.seth(270)
    self.turtle.shape("square")
    self.turtle.pu()

    

    self.x = 0
    self.y = 0
    self.xper = [0,0]
    self.yper = [0,0]
    self.onclickfunc = placeholder
    self.width = 0
    self.widthper = [0,0]
    self.height = 0
    self.heightper = [0,0]
    self.color = "000000"
    self.textcolor = "000000"
    self.fontfamily = "Sans Serif"
    self.fontsize = 16
    self.fonttype = 'normal'
    self.content = ''
    self.hidden = False

    elements.append(self)

  def hide(self):
    """
    Hides the element from view and makes it intangible 
    """
    self.hidden = True
    self.turtle.ht()
    self.turtle.goto(-1000,-1000)
    self.wturtle.clear()

  def show(self):
    """
    Brings the element back into view and makes it tangible again after being hidden
    """
    if(self.hidden == True):
      self.hidden = False
      self.turtle.st()
      self.render()

  def setdata(self,userdata):
    """
    Assign any data you want to the element
    """
    self.data = userdata

  def setx(self,xgiven: int):
    """
    Set the x-coordinate location of the element in pixels. Every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.x = xgiven

  def setxpercent(self,xgiven: int):
    """
    Set the x-coordinate location of the element in a percentage of the screen size (0 to 100). Every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.xper = [(win.winfo_screenwidth() * userconfig["SCREEN_SIZE"][0]) * (xgiven / 100),xgiven]

  def sety(self,ygiven: int):
    """
    Set the y-coordinate location of the element in pixels. Every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.y = ygiven

  def setypercent(self,ygiven: int):
    """
    Set the y-coordinate location of the element in a percentage of the screen size (0 to 100). Every element starts at the top-left, and their origin is at the top left of itself
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.yper = [(win.winfo_screenheight() * userconfig["SCREEN_SIZE"][1]) * (ygiven / 100),ygiven]

  def setwidth(self,xgiven: int):
    """
    Set the visual width of the element in pixels
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.width = xgiven

  def setwidthpercent(self,xgiven: int):
    """
    Set the visual width of the element in percentage of the screen width (0 to 100)
    """
    if not isinstance(xgiven,int):
      raise TypeError("x must be an integer")
    self.widthper = [(win.winfo_screenwidth() * userconfig["SCREEN_SIZE"][0]) * (xgiven / 100),xgiven]

  def setheight(self,ygiven: int):
    """
    Set the visual height of the element in pixels
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.height= ygiven

  def setheightpercent(self,ygiven: int):
    """
    Set the visual height of the element in percentage of the screen height (0 to 100)
    """
    if not isinstance(ygiven,int):
      raise TypeError("y must be an integer")
    self.heightper = [(win.winfo_screenheight() * userconfig["SCREEN_SIZE"][1]) * (ygiven / 100),ygiven]

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
    print(func)
    if(callable(func)):
      self.onclickfunc = func
    elif(func == "disable"):
      self.onclickfunc = placeholder
    else:
      raise TypeError("argument must be a function")

def finish():
  t.done()
    
def __click__(data):
  print(data)
  for _,element in enumerate(elements):
    calcx = int(element.x + element.xper[0])
    calcy = int(element.y + element.yper[0])
    calcw = int(element.width + element.widthper[0])
    calch = int(element.height + element.heightper[0])
    if(data.x in range(calcx,calcx + calcw) and data.y in range(calcy,calcy + calch)):
      element.onclickfunc(element)

def __config__(data):
  for _,ob in enumerate(elements):
    ob.xper = [(win.winfo_screenwidth() * userconfig["SCREEN_SIZE"][0]) * (ob.xper[1] / 100),ob.xper[1]]
    ob.yper = [(win.winfo_screenheight() * userconfig["SCREEN_SIZE"][0]) * (ob.yper[1] / 100),ob.yper[1]]
    ob.widthper = [(data.width) * (ob.widthper[1] / 100),ob.widthper[1]]
    ob.heightper = [(data.height) * (ob.heightper[1] / 100),ob.heightper[1]]
    ob.render()

def forcequit():
  win.quit()
  t.bye()

def reconfig():
  screen.setup(userconfig["SCREEN_SIZE"][0],userconfig["SCREEN_SIZE"][1])
  win.resizable(userconfig["RESIZABLE"],userconfig["RESIZABLE"])
  
  
  win.title(userconfig["TITLE"])
  if(platform.system() == 'Windows' and userconfig["WINDOWS_DISABLED"] == True) or (platform.system() == 'Darwin' and userconfig["MAC_DISABLED"] == True) or (platform.system() == 'Linux' and userconfig["LINUX_DISABLED"] == True):
    msg.showerror("Operating System Restricted","The developer of this application has disabled usage on this particular operating system. Sorry for any inconvenience")
    forcequit

reconfig()

    
#t.onscreenclick(click)
ws = t.getcanvas()
ws.bind('<Button-1>',__click__)
ws.bind('<Configure>',__config__)

#def pause():
#  if True:
#    t.ontimer(pause,250)