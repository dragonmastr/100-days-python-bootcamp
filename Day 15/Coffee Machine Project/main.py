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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO 1. Check resources sufficient?
def is_resource_availability(order_ingredient):
    for i in order_ingredient:
        if order_ingredient[i] > resources[i]:
            print("Sorry out of resources")
            return False
    return True

# TODO 2. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


#TODO 3. check transaction successful
def is_transaction_successful(payment, cost):
    if payment >= cost:
        change = round(payment - cost,2)
        print(f"Here's your {change}")
        global profit
        profit +=cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



#TODO 4. Make Coffee
def make_coffee(choice,drink):
    for i in drink:
        resources[i] = resources[i] - drink[i]
    print(f"Here's you {choice} .. enjoy ☕")


is_on= True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("the current resources values:\n")
        print(f"Water: {resources["water"]}ml")
        print(f"Water: {resources["milk"]}ml")
        print(f"Water: {resources["coffee"]}g")
        print(f"Money ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_availability(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])










