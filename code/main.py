from turtle import Screen
from make_coffee import MakeCoffee, CoffeePrice
from money import Money
import time

#Setting up the screen
screen = Screen()
screen.setup(900, 600)
screen.tracer(0)
screen.title("Wending Machine")
screen.bgcolor("#ede3ca")
screen.bgpic("welcome.png")

#Creating objects of our classes
latte_cost = CoffeePrice()
cappuccino_cost = CoffeePrice()
espresso_cost = CoffeePrice()
coffee = MakeCoffee()
money = Money()

#Update our screen with the next image, along with coffee prices
screen.update()
time.sleep(3)
screen.bgpic("coffeetypes.png")

#Writing prices of our coffees on the second bg image ("coffee types") - just for UI purposes
latte_cost.price_write(-320, -180, 2.5)
cappuccino_cost.price_write(-10, -180, 3)
espresso_cost.price_write(300, -180, 1.5)
screen.update()
time.sleep(2)

#Ask user for their initial input
user_coffee = screen.textinput("Coffee Type", "What would you like to have at our coffee bar?").lower()

while user_coffee != "off":                                                     #While will run till the user types "off"
    user_change = 0
    if user_coffee == "report":                                                 #If user types "report"
        latte_cost.clear()                                                      #All the coffee prices will be cleared from the screen and user will be taken to a different screen
        cappuccino_cost.clear()
        espresso_cost.clear()
        coffee.gen_report()                                                     #From the class MakeCoffee, we call the gen_report function

    else:                                                                       #Otherwise, user would have entered the kind of coffee he wants to drink
        coffee.check_resources(user_coffee)                                     #From the class MakeCoffee, we call the check_resources function
        if coffee.resources:                                                    #If we have enough resources for that coffee
            user_payment = money.enter_money()                                  #From the class Money, we call the enter_money function so the user could enter his/her payment
            latte_cost.clear()                                                  #We clear all the coffee machine's cost from the screen, as we will now go to a different screen
            cappuccino_cost.clear()
            espresso_cost.clear()
            user_change = money.user_transaction(user_coffee, user_payment)     #From the class Money, we call the user_transaction function to get change if any for the user
            if money.transaction:                                               #If the transaction went well
                screen.bgpic("preparingcoffee.png")                             #We will go to the screen of "preparingcoffee"
                screen.update()
                time.sleep(3)
                if user_change > 0:                                             #If user has any change
                    money.print_change(user_change)                             #We will print it on screen
                coffee.make_coffee(user_coffee)                                 #From the class MakeCoffee, we will call the make_coffee function
            else:
                screen.bgpic("nomoney.png")                                     #Otherwise, go to the screen showing user did not put in enough cash

        latte_cost.clear()                                                      #Clear all the coffee costs from the screen incase any of the above-mentioned events fail
        cappuccino_cost.clear()                                                 #E.g, user did not have enough cash or machine did not have enough resources
        espresso_cost.clear()

    screen.update()
    time.sleep(3)
    coffee.restart(latte_cost, cappuccino_cost, espresso_cost, money)           #From the class MakeCoffee, we will call the restart function
    user_coffee = screen.textinput("Coffee Type", "What would you like to have (Espresso/Latte/Cappucino)? ").lower()

screen.exitonclick()                                                             #Screen will close only when the user presses "X"
