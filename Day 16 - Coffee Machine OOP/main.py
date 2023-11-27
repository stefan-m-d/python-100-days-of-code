from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
flag = True

while flag != False:
    
    drink = input("What would you like? (espresso/latte/cappuccino): ")
   
    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    
    elif drink == "off":
        flag = False
        exit()
    
    else: 
        
        find_item = menu.find_drink(drink)
        
        can_make = coffee_maker.is_resource_sufficient(find_item)
        
        if can_make == False: 
            continue
        
        else: 
            
            make_payment = money_machine.make_payment(find_item.cost)
            
            if make_payment == False: 
                continue
            
            else: 
                coffee_maker.make_coffee(find_item)
