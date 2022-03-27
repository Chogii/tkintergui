import enum
import tkintergui as gui 

order = []

menu = {
    "Burgers": {
        "__config__":{
            'headercolor':'FF0000'
        },
        "Cheeseburger":{
            "price":150,
            "features":["Bread","Meat","Ketchup","Mustard","Onions"]
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

for catindex,cat in enumerate(menu):
    catObject = menu[cat]
    config = catObject["__config__"]
    header = gui.Element()
    header.setcontent(cat)
    header.settextcolor("FFFFFF")
    header.setcolor(config['headercolor'])
    header.setwidth(200)
    header.setheight(50)
    header.setx(catindex * 200)
    header.render()

    for itemindex,item in enumerate(catObject):
        itemObject = catObject[item]
        if item.startswith('__') != True :
            itembox = gui.Element()
            itembox.setcontent(item)
            itembox.setx(header.x)
            itembox.sety(itemindex * 50)
            itembox.setwidth(200)
            itembox.setheight(50)
            itembox.setcolor("000000")
            itembox.settextcolor("FFFFFF")
            itembox.render()




gui.finish()