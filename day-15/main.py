MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

off = False
profit = float(0)

def makeDrink(drink):
    global profit
    if drink in MENU:
        ingredients_needed = MENU[drink]["ingredients"]
        can_make = True
        # extract values from a dictionary, and assign them to variables
        for ingredient, amount_needed in ingredients_needed.items():
            if ingredient in resources and resources[ingredient] >= amount_needed:
                resources[ingredient] -= amount_needed
            else:
                can_make = False
                print(f"Sorry, not enough {ingredient}.")
                break
        if can_make:
            print(f"Here is your {drink} ☕. Enjoy!")
        else:
            print(f"Cannot make a {drink}.")
    else:
        print("Invalid drink choice. Please choose from the menu.")


def transaction(insert_quarters, insert_dimes, insert_nickles, insert_pennies, order):
    global profit
    value = float((insert_quarters * 0.25) + (insert_dimes * 0.10) + (insert_nickles * 0.05) + (insert_pennies * 0.01))
    print(f"You inserted ${value:.2f}")

    if(value >= MENU[order]["cost"]):
        profit += MENU[order]["cost"]
        change = value - MENU[order]["cost"]
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

while not off:
    order = input("What would you like? (espresso/latte/cappuccino) or a report? ").lower()

    if order == "report":
        print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g.\nMoney: ${profit:.2f}")
    elif order == "off":
        print("Turning off the machine.")
        off = True
    else:
        print(f"It will cost: ${MENU[order]['cost']:.2f}")
        print("Please, insert coins:")
        insert_quarters = float(input("How many quarters? "))
        insert_dimes = float(input("How many dimes? "))
        insert_nickles = float(input("How many nickles? "))
        insert_pennies = float(input("How many pennies? "))
        transactionCheck = transaction(insert_quarters, insert_dimes, insert_nickles, insert_pennies, order)

        if transactionCheck == True:
            makeDrink(order)
