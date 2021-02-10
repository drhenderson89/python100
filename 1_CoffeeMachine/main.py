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
    print("Water: {0}ml".format(resources['water']))
    print("Milk: {0}ml".format(resources['milk']))
    print("Coffee: {0}".format(resources['coffee']))
    print("Money: £{0}".format(resources['money']))

# Check drink requirements against resources
def checkDrinkResources(drink):
    try:
        for ingredient in MENU[drink]['ingredients']:
            if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
                print('Sorry there is not enough {}.'.format(ingredient))
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
    change = coins - MENU[drink]['cost']
    print("Here is £{:.2f} pounds in change.".format(change))
    return change

def makeDrink(drink):
    for ingredient in MENU[drink]['ingredients']:
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    print("Here is your {}. Enjoy!".format(drink))

# Main loop, actions taken on condition of text
text=""
power=0
while(power==0):
    text = input("What would you like? (espresso/latte/cappuccino):")
    if text.lower() == 'off':
        power = 1
    elif text.lower() == "report":
        report()
    else:
        if(checkDrinkResources(text.lower())):
            total = getCoins()
            if(checkAmount(total, text.lower())):
                change = dispenseChange(total, text.lower())
                resources['money'] += (total-change)
                makeDrink(text.lower())
            else:
                print("Sorry that's not enough money. Money refunded.")

