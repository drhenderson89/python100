# Basic coffee machine information
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

# Manage resources when low
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Output current resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: £{resources['money']}")

# Check drink requirements against resources
def checkDrinkResources(drink):
    try:
        for ingredient in MENU[drink]['ingredients']:
            if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
                print(f'Sorry there is not enough {ingredient}.')
                return False
        return True
    except:
        print("Invalid drink choice")
        return False

# Process inserted coins
def getCoins():
    quarters = float(input("Insert quarters:"))
    dimes = float(input("Insert dimes:"))
    nickles = float(input("Insert nickels:"))
    pennies = float(input("Insert pennies:"))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

# Check successful transaction
def checkAmount(coins, drink):
    return coins > MENU[drink]['cost']

def dispenseChange(coins, drink):
    change = round(coins - MENU[drink]['cost'],2)
    print(f"Here is £{change} pounds in change.")
    return change

def makeDrink(drink):
    for ingredient in MENU[drink]['ingredients']:
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    print(f"Here is your {drink}. Enjoy!")

# Main loop, actions taken on condition of text
text=""
power=0
while(power==0):
    text = input("What would you like? (espresso/latte/cappuccino):").lower()
    if text == 'off':
        power = 1
    elif text == "report":
        report()
    else:
        if(checkDrinkResources(text)):
            total = getCoins()
            if(checkAmount(total, text)):
                change = dispenseChange(total, text)
                resources['money'] += round((total-change),2)
                makeDrink(text)
            else:
                print("Sorry that's not enough money. Money refunded.")
