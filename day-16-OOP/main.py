# from turtle import Turtle, Screen
#
# bob = Turtle()
# bob.shape("turtle")
# bob.color("purple")
# bob.forward(100)
#
# my_screen = Screen()
# my_screen.canvheight
# my_screen.exitonclick()
#

# PyPi

# from prettytable import PrettyTable
#
# table = PrettyTable()
# print(table)
#
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type",["Eletric", "Water", "Fire"])
# table.align = "r"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
end = False

while not end:
    items = menu.get_items()
    order = input(f"What would you like? ({items}) or a report? ").lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        print("Turning off the machine.")
        end = True
    else:
        drink = menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
