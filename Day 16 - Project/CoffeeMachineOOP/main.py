from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)

#Create objects
coffee_maker = CoffeeMaker()
options = Menu()
money_machine = MoneyMachine()

order_complete = False
while not order_complete:
    #Ask user for their drink order
    order = input(f"What would you like? ({options.get_items()}): ").lower()

    #Review what user inputted
    if order == "report": #Get report
        coffee_maker.report()
        money_machine.report()
    elif order == "off": #Turn off the machine
        order_complete = True
    else: #Make drink
        #Check that the drink exists
        if options.find_drink(order) != "None": #It exists
            #Get ingredients and costs for the drinks on the menu
            item_ingredients = {}
            item_cost = {}
            item_option = {}
            for item in options.menu:
                item_ingredients[item.name] = item.ingredients
                item_cost[item.name] = item.cost
                item_option[item.name] = item

            #Check that there are enough resources in the machine to make the selected drink
            if coffee_maker.is_resource_sufficient(item_option[order]): #There is enough
                #Collect payment
                if money_machine.make_payment(item_cost[order]): #Payment is sufficient
                    #Make drink
                    coffee_maker.make_coffee(item_option[order])
        else: #It does not exist
            print("Sorry, that drink is not available.")