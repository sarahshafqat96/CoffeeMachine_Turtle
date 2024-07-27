from turtle import Turtle
import ingredients
import time


class MakeCoffee(Turtle):                                                   #Creating MakeCoffee class
    def __init__(self):
        super().__init__()                                                  #Turtle as its super class
        self.ingredient = ""                                                #Initially the ingredient variable will be empty
        self.color("#6F4E37")                                               #Turtle's color will be coffee brown
        self.resources = False                                              #Intially the resources variable will be False
        self.hideturtle()                                                   #Hide the turtle
        self.penup()                                                        #Turtle should not leave any trace lines

    def restart(self, latte, cappuccino, espresso, money_ob):               #Restart function will be called when user wants to start the game from the first screen
        money_ob.clear()                                                    #Object of class Money will be cleared
        self.clear()                                                        #Screen will be cleared
        self.screen.bgcolor("#ede3ca")                                      #Screen's bg color will be set to skin
        self.screen.bgpic("welcome.png")                                    #Screen's bg picture will be set to "welcome"
        self.screen.update()
        time.sleep(3)
        self.screen.bgpic("coffeetypes.png")                                #After 3 seconds, Screen's bg picture will be set to "coffeetypes"
        latte.price_write(-320, -180, 2.5)                                  #Prices of those coffee's will be written on that screen
        cappuccino.price_write(-10, -180, 3)
        espresso.price_write(300, -180, 1.5)
        self.screen.update()                                                #After 2 seconds that screen will change to the next function's
        time.sleep(2)

    def gen_report(self):                                                   #Function to create report of the resources
        self.goto(0, -50)                                                   #Turtle will go to the center
        self.screen.bgpic("report_bg.png")                                  #Screen's bg picture will be set to "report_bg"
        Water = ingredients.resources['water']                              #Variables containing current amounts of our resources will be created
        Milk = ingredients.resources['milk']
        Coffee = ingredients.resources['coffee']
        self.write(f"Water = {Water} ml\nMilk = {Milk} ml\nCoffee = {Coffee} g", False, align="center",
                   font=("Candara", 30, "bold"))                            #Turtle will print those amounts along with resource names in the middle of the screen

    def check_resources(self, user_drink):                                  #Function to check resources of the drink user entered
        drink_ingredients = ingredients.MENU[user_drink]['ingredients']     #Find the ingredients of those drink from ingredients.py file
        for key in drink_ingredients:                                       #For loop through the ingredients
            if ingredients.resources[key] < drink_ingredients[key]:         #If the resources are less than required for the drink
                self.ingredient = key                                       #Store that resource in the class's ingredient variable
                self.resources = False                                      #Set the class's resource variable to False
                break                                                       #Break out of the loop
        if self.ingredient == "water":                                      #Check which resource was finished and display its respective screen
            self.screen.bgpic("nowater.png")
        elif self.ingredient == "coffee":
            self.screen.bgpic("nocoffee.png")
        elif self.ingredient == "milk":
            self.screen.bgpic("nomilk.png")
        else:
            self.resources = True                                           #Otherwise, class's resource variable will be true

    def make_coffee(self, user_drink):                                      #Function for creating user's coffee
        self.clear()                                                        #Clear everything on the screen
        self.goto(0, -240)                                                  #Turtle goes to these co-ordinates
        drink_resources = ingredients.MENU[user_drink]['ingredients']       #Find the ingredients of those drink from ingredients.py file
        for key in drink_resources:                                         #For every ingredient
            ingredients.resources[key] -= drink_resources[key]              #Subtract it from the available resources
        if user_drink == "cappuccino":                                      #Depending upon the user's drink, display the respective image
            self.screen.bgpic("cappuccino.png")
        elif user_drink == "latte":
            self.screen.bgpic("latte.png")
        else:
            self.screen.bgpic("espresso.png")
        self.write(f"Here is your {user_drink}. Enjoy!", False, align="center",
                   font=("Quire Sans Light Italic", 20, "normal"))          #Print user's change on the screen and "enjoy the drink"


class CoffeePrice(Turtle):                                                  #Creating CoffeePrice class
    def __init__(self):
        super().__init__()                                                  #Turtle as its super class
        self.hideturtle()                                                   #Hide the turtle
        self.penup()                                                        #Turtle should not leave any traces
        self.color("#6F4E37")                                               #Turtle's color will be coffee brown

    def price_write(self, x_pos, y_pos, price):                             #Function to write the price of coffee on the screen
        self.teleport(x_pos, y_pos)
        self.write(f"${price}", False, align="center", font=("Quire Sans Light Italic", 20, "bold"))
