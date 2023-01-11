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
money=0
is_on=True
def is_resources_sufficient(order_ingredients):
    """Returns True if there are sufficient_resources, returns False if there is not. """
    for items in order_ingredients:
        if order_ingredients[items]>resources[items]:
            print(f"Sorry, not enough {items}.")
            return False
    return True
def process_coins():
    """Returns the total ammount of coins inserted"""
    print("Insert coins.")
    total=int(input("How many quarters: "))*0.25
    total+=int(input("How many dimes: "))*0.10 
    total+=int(input("How many nickles: "))*0.05
    total+=int(input("How many cents: "))*0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    """Returns True if transaction is successful, returns False if it is not."""
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global money 
        money+=drink_cost
        return True
    else:
        print("Sorry, not enough money. Coins refunded.")
        return False
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from resources"""
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f"Here is your {drink_name}. Enjoy!")
def add_resources(order_ingredients):
    add=input("Do you wanna add water, milk or coffee?\n").lower()
    if add=="water":
        quantity=int(input("How much water do you wanna add in ml?\n"))
        order_ingredients["water"]+=quantity
    elif add=="milk":
        quantity=int(input("How much milk do you wanna add in ml?\n"))
        order_ingredients["milk"]+=quantity
    elif add=="coffee":
        quantity=int(input("How much coffee do you wanna add in gm?\n"))
        order_ingredients["coffee"]+=quantity
    print("The ingredient has been added to the machine.")
while is_on:
    choice=input("What drink do you want? Espresso ($1.5), Cappuccino ($3) or Latte ($2.5). Type 'report' to see ingredient report, type 'off' to turn off the machine or type 'add' to add ingredients in the machine.\n").lower()
    if choice=="report":
        print(f"Water: {resources['water']} ml.")
        print(f"Milk: {resources['milk']} ml.")
        print(f"Coffee: {resources['coffee']} g.")
        print(f"Money: ${money}")
    elif choice=="off":
        is_on=False
        print("Adios")
    elif choice=="add":
        add_resources(resources)
    elif choice=="espresso" or choice=="cappuccino" or choice=="latte":
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
    else:
      is_on=False
      print("Invalid input. Restart the program and try again.")
            
                
