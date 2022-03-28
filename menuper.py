import tkintergui as gui
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

total = 0
xpush = 0

for catIndex,catName in enumerate(menu):
    catObject = menu[catName]
    catConfig = catObject["__config__"]
    catHeader = gui.Element()
    catHeader.setcontent(catName)
    catHeader.setwidthpercent(20)
    catHeader.setxpercent(xpush)
    xpush += 20
    catHeader.setheightpercent(5)
    catHeader.setcolor(catConfig['headercolor'])
    catHeader.settextcolor("FFFFFF")
    catHeader.render()

gui.finish()