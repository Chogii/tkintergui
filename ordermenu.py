import enum
import tkintergui as gui 

menu = {
    "Burgers": {
        "__config__":{
            'headercolor':'FF0000'
        }
    },
    "Sides": {
        "__config__":{
            'headercolor':'19BC00'
        }
    },
    "Drinks": {
        "__config__":{
            'headercolor':'0000FF'
        }
    },
    "Desserts": {
        "__config__":{
            'headercolor':'FF00FF'
        }
    }
}

for i,item in enumerate(menu):
    itemObject = menu[item]
    config = itemObject["__config__"]
    element = gui.Element()
    element.setcontent(item)
    element.settextcolor("FFFFFF")
    element.setcolor(config['headercolor'])
    element.setwidth(200)
    element.setheight(50)
    element.setx(i * 200)
    element.render()


gui.finish()