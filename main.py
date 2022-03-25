import turtle as t
screen = t.Screen()
t.penup()
t.forward(1)
#t.ht()
t.speed('fastest')
global cur
cur = None
global buttons
buttons = []

defaults = {
    'fontsize':16,
    'fontfamily':'Arial Bold',
    'fonttype':'normal',
    'textcolor':'#000000'
}

elements = [
  {
    'class': 'button',
    'color':"#32a852",
    'x':0,
    'y':0,
    'width':200,
    'height':50,
    'content':'Click Here',
    'textcolor':'#FFFFFF',
    'fontsize':28,
    'fontfamily':'Sans Serif'
  }  
]

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
  def __init__(self):
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0
    self.color = "000000"
    self.textcolor = "000000"
    self.fontfamily = "Sans Serif"
    self.fontsize = 16
    self.fonttype = 'normal'
    self.content = ''

    self.rendered = False
    print("Hello World!")

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

  def render(self):
    if(self.rendered == False):
      self.rendered = True
      t.setx(self.x)
      t.sety(self.y)
      t.color("#" + self.color)
      t.seth(0)
      t.pendown()
      t.begin_fill()
      for i in range(2):
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
      t.end_fill()



def ignore():
  None

def adjustPos():
  t.setx(cur['x'])
  t.sety(cur['y'])
  
def drawElement():
    if 'color' in cur:
        t.color(cur['color'])
    t.seth(0)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(cur['width'])
        t.left(90)
        t.forward(cur['height'])
        t.left(90)
    t.end_fill()
    #content
    if('content' in cur):
        if 'textcolor' in cur:
            t.color(cur['textcolor'])
        else:
            t.color(defaults['textcolor'])

        fontfam = defaults['fontfamily']
        fontsize = defaults['fontsize']
        fonttype = defaults['fonttype']

        t.penup()
        t.setpos( ((cur['x'] + cur['width']) / 2) , ((cur['y'] + cur['height']) / 2) - (fontsize))
        t.pendown

        if('fontfamily' in cur):
            fontfam = cur['fontfamily']
        if('fontsize' in cur):
            fontsize = cur['fontsize']
        if('fonttype' in cur):
            fonttype = cur['fonttype']

        t.write(cur['content'],True,"Center",[fontfam,fontsize,fonttype])
    t.penup()

callbackRef = {
  'x':adjustPos,
  'y':ignore,
  'width':drawElement,
  'height':ignore,
  'class':ignore,
  'content':ignore,
  'color':ignore,
  'textcolor':ignore,
  'fontfamily':ignore,
  'fontsize':ignore,
  'fonttype':ignore
}

# this was for testing

#for ind1,element in enumerate(elements):
#  cur = element
#  if(element['class'] == 'button'):
#      buttons.append([[element['x'],element['y']],[element['width'],element['height']]]) 
#  for ind2,prop in enumerate(element):
#    callbackRef[prop]()
    
def click(x,y):
  for _,button in enumerate(buttons):
      if(x in range(button[0][0],button[1][0]) and y in range(button[0][1],button[1][1])):
          print("Hello World!")

    
t.onscreenclick(click)

t.done()