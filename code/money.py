from turtle import Turtle
import ingredients


class Money(Turtle):                                                                    #Creating Money class
    def __init__(self):
        super().__init__()                                                              #Turtle as its super class
        self.hideturtle()                                                               #Hide the turtle
        self.penup()                                                                    #Turtle should not leave any trace lines
        self.transaction = False                                                        #Initially the transaction variable will be False
        self.goto(0, 160)                                                         #Turtle's position
        self.color("#6F4E37")                                                           #Turtle's color will be coffee brown

    def enter_money(self):                                                              #Function to get user's money
        money = self.screen.textinput("Money: ", "Please enter the money as: Quarters, Dimes, Nickles, Pennies")
        quarters, dimes, nickles, pennies = money.split(",")                            #Split the money in these variables
        total_money = (round((int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) * 0.01), 2))
        return total_money                                                              #Convert money into $ and return it

    def user_transaction(self, drink_type, user_money):                                 #Function to evaluate whether user's money is enough for their drink or not
        self.clear()                                                                    #Clear the screen
        if user_money < ingredients.MENU[drink_type]['cost']:                           #If user's money is less than the cost
            self.transaction = False                                                    #Set the transaction variable to False
        else:
            ingredients.profit += ingredients.MENU[drink_type]['cost']                  #Otherwise add that cost to the profit variable in ingredients.py
            if user_money > ingredients.MENU[drink_type]['cost']:                       #If user entered more money than the cost
                change = round(user_money - ingredients.MENU[drink_type]['cost'], 2)    #Calculate change
                self.transaction = True                                                 #Set the transaction variable to True
                return change                                                           #And return change

    def print_change(self, payment_change):                                             #Function to print user's change on the screen
        self.goto(0, 220)                                                         #Turtle will go to this position
        self.write(f"HERE IS ${payment_change} DOLLARS IN CHANGE", False, align="center",
                    font=("Candara", 20, "normal"))                                     #Write the change on the screen
