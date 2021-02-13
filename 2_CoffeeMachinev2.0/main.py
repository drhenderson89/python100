from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
drinks_menu = Menu()
coffe_machine = CoffeeMaker()
moneybox = MoneyMachine()

while is_on:
    text = input(f"What would you like? {drinks_menu.get_items()}:").lower()
    if text == 'off':
        is_on = False
    elif text == 'report':
        coffe_machine.report()
    else:
        drink = drinks_menu.find_drink(text)
        if(drink):
            if(coffe_machine.is_resource_sufficient(drink)):
                if(moneybox.make_payment(drink.cost)):
                    coffe_machine.make_coffee(drink)

