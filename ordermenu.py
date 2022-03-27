import enum
import tkintergui as gui 

order = {}

menu = {
    "Meals": {
        "__config__":{
            'headercolor':'FF0000'
        },
        "Cheeseburger":{
            "price":150,
            "features":["Bread","Meat","Ketchup","Mustard","Onions"]
        },
        "Bacon Burger":{
            "price":270,
            "features":["Bread","Bacon","Meat","Ketchup","Mustard","Onions"]
        },
        "Big Burger":{
            "price":350,
            "features":["Bread","Meat","Meat","Ketchup","Mustard","Onions"]
        },
        "Chicken Sandwich":{
            "price":300,
            "features":["Bread","Chicken","Mayonaise","Lettuce","Pickles"]
        },
        "Spicy Chicken Sandwich":{
            "price":350,
            "features":["Bread","Chicken","Spicy Sauce","Pickles"]
        },
        "Chicken Nuggets":{
            "price":300,
            "features":["Sauce"]
        },
        "Chicken Tenders":{
            "price":370,
            "features":["Sauce"]
        },
    },
    "Sides": {
        "__config__":{
            'headercolor':'19BC00'
        },
        "Fries":{
            "price":200,
            "features":["Salt","Ketchup"]
        },
        "Fry Basket":{
            "price":430,
            "features":["Salt","Ketchup"]
        },
        "Mac and Cheese":{
            "price":320,
            "features":[]
        },
        "Mashed Potatoes":{
            "price":350,
            "features":["Gravy","Salt"]
        },
        "Red Beans and Rice":{
            "price":300,
            "features":[]
        },
    },
    "Drinks": {
        "__config__":{
            'headercolor':'0000FF'
        },
        "Coca-Cola":{
            "price":100,
            "features":["Ice"]
        },
        "Dr. Pepper":{
            "price":100,
            "features":["Ice"]
        },
        "Sprite":{
            "price":100,
            "features":["Ice"]
        },
        "Mountain Dew":{
            "price":150,
            "features":["Ice"]
        },
        "Root Beer":{
            "price":100,
            "features":["Ice"]
        },
        "Sweet Iced Tea":{
            "price":150,
            "features":["Ice"]
        },
        "Unsweet Iced Tea":{
            "price":130,
            "features":["Ice"]
        },
    },
    "Desserts": {
        "__config__":{
            'headercolor':'FF00FF'
        },
        "Ice Cream Cone":{
            "price":160,
            "features":["Chocolate Dunked"]
        },
        "Sundae":{
            "price":350,
            "features":["Chocolate Fudge","Sprinkles","Cherry"]
        },
        "Funnel Cake":{
            "price":480,
            "features":["Powdered Sugar","Chocolate Drizzle","Sprinkles"]
        },
        "Apple Pie":{
            "price":700,
            "features":[]
        },
    }
}

xreach = 0
total = gui.Element()


def updateTotal():
    amount = 0
    pretty = ""
    for _,item in enumerate(order):
        itemObject = order[item]
        amount += itemObject["price"]
    amount = amount / 100
    pretty = "Total: $" + str(amount)
    if(pretty[-2] == "."):
        pretty += "0"
    total.setcontent(pretty)
    total.render()

def addTo(element):
    itemObject = element.data[1]
    itemName = element.data[0]
    try:
        del order[itemName]
        element.setcolor("000000")
        element.settextcolor("FFFFFF")
    except:
        order[itemName] = itemObject
        element.setcolor("32A852")
        element.settextcolor("000000")
    element.render()
    updateTotal()


for catindex,cat in enumerate(menu):
    catObject = menu[cat]
    config = catObject["__config__"]
    header = gui.Element()
    header.setcontent(cat)
    header.settextcolor("FFFFFF")
    header.setcolor(config['headercolor'])
    header.setwidth(200)
    xreach += 200
    header.setheight(50)
    header.setx(catindex * 200)
    header.render()

    for itemindex,item in enumerate(catObject):
        itemObject = catObject[item]
        if item.startswith('__') != True :
            temp = "$" + str(itemObject['price'] / 100)
            if(temp[-2] == "."):
                temp += "0"

            itembox = gui.Element()
            itembox.setcontent(item + " - " + temp)
            itembox.setx(header.x)
            itembox.sety(itemindex * 50)
            itembox.setwidth(200)
            itembox.setheight(50)
            itembox.setcolor("000000")
            itembox.settextcolor("FFFFFF")
            itembox.setdata([item,itemObject])
            itembox.onclick(addTo)
            if len(item + temp) > 12:
                itembox.setfontsize(12)
            if len(item + temp) > 18:
                itembox.setfontsize(10)

            itembox.render()

total.setx(xreach)
total.setcolor("FFFFFF")
total.settextcolor("000000")
total.setfontsize(20)
total.setwidth(300)
total.setheight(75)
total.setcontent("Total: $0.00")
total.render()


gui.finish()