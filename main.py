MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0
missing_ingredient = []
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
change = 0
sum_of_coins = 0


def report_resources():
    """Shows current amount of resources available in the coffee machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def is_sufficient():
    """Checks if current amount of resources available in the coffee machine are enough to make an order."""
    global missing_ingredient
    needed_water = MENU[order]["ingredients"]["water"]
    needed_milk = MENU[order]["ingredients"]["milk"]
    needed_coffee = MENU[order]["ingredients"]["coffee"]
    if resources["water"] < needed_water:
        missing_ingredient.append("water")
    if resources["milk"] < needed_milk:
        missing_ingredient.append("milk")
    if resources["coffee"] < needed_coffee:
        missing_ingredient.append("coffee")

    if len(missing_ingredient) > 0:
        return False
    return True


def process_coins():
    global change
    global sum_of_coins
    num_of_quarters = int(input("How many quarters? "))
    num_of_dimes = int(input("How many dimes? "))
    num_of_nickels = int(input("How many nickels? "))
    num_of_pennies = int(input("How many pennies? "))

    sum_of_coins = round(
        (num_of_quarters * quarter) + (num_of_dimes * dime) + (num_of_nickels * nickel) + (num_of_pennies * penny), 2)
    if sum_of_coins >= MENU[order]["cost"]:
        change += round((sum_of_coins - MENU[order]["cost"]), 2)
        return True
    else:
        return False


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO: 2. Print report of all coffee machine resources
# TODO: 3. Check resources sufficient to make drink order
# TODO: 4. Process coins
# TODO: 5. Check transaction successful?
# TODO: 6. Make coffee

is_coffee_machine_on = True

while is_coffee_machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        report_resources()
    elif order == "off":
        is_coffee_machine_on = False
    else:
        if is_sufficient():
            if process_coins():
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                money += round((sum_of_coins - change), 2)
                print(f"Returning change: ${change}.")
                print(f"Here is your {order}. Enjoy!")
            else:
                print(f"Not enough coins, returning full amount of money: {sum_of_coins}")
        else:
            print(f"Sorry there is not enough: {' '.join(missing_ingredient)}.")
