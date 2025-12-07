from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from prettytable import PrettyTable

table = PrettyTable()
money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
print(table.add_column("Item",["latte","espresso","cappuccino"]))
while True:
    choice = menu.get_items()
    choice_menu = input(f"what would you like? {choice}")
    if choice_menu == "off":
        break
    elif choice_menu == "report":
        (coffee.report())
        (money.report())
    # coin = money.process_coins()
    # print(f"Here is ${coin}")
    else:
        drink = menu.find_drink(choice_menu)
        if coffee.is_resource_sufficient(drink)and money.make_payment(drink.cost):
            coffee.make_coffee(drink)

