# machine requirements - 
# 1 print report - what's left and how much - water, milk, coffee, money
# 2 check resources sufficient - if a user orders a drink and there are not enough resources, don't make drink and refund user
# 3 check money given - if not enough, refund user, if enough - make drink 
# 4 count coins - how much is given and how much should be returned

import menu
money = 0.00
resources_local = menu.resources

print ("Type info on the drink prompt to receive some drink information")

# get the chosen drink's ingredients

def returningredients(drink_requested):
            drink_requested = menu.MENU.get(drink_requested)
            ingredients = drink_requested['ingredients']
            return ingredients


# get the chosen drink's price

def returnprice(drink_requested): 
    drink_requested = menu.MENU.get(drink_requested)
    cost = drink_requested['cost']
    return cost
    
#coffee machine go brr    

flag = True

while flag != False:
    
    drink = input("What would you like? (espresso/latte/cappuccino): ")
   
    if drink == "report":
        print (f"Water: {resources_local['water']}ml \nMilk: {resources_local['milk']}ml \nCoffee: {resources_local['coffee']}g \nMoney: {money}$ \n")
    
    #easter egg
    
    elif drink == "info":
        print ("TUK NE E INFORMACIA!!!")
        flag = False
        exit()
    
    # turn machine off
    
    elif drink == "off":
        flag = False
        exit()
    
    else: 
    #get specified drink's ingredients
        
        ingredients = returningredients(drink_requested=drink)
    
        if 'milk' not in ingredients:
            ingredients['milk'] = 0
    
    #check supplies
    
        if ingredients['water']>resources_local['water']:
        
            print ("Sorry, there is not enough water to make your drink")
        
        
        elif drink != "espresso" and ingredients['milk']>resources_local['milk']:
        
            print ("Sorry, there is not enough milk to make your drink")
        
        
        elif ingredients['coffee']>resources_local['coffee']:
        
            print ("Sorry, there is not enough coffee to make your drink")
        
        
    #get coins
        
        else: 
        
            print ("Please insert coins.")
        
            input_quarters = int(input("How many quarters: "))
            input_dimes = int(input("How many dimes: "))
            input_nickels = int(input("How many nickels: "))
            input_pennies = int(input("How many pennies: "))
        
            sum_input = input_quarters*0.25 + input_dimes*0.10 + input_nickels*0.05 + input_pennies*0.01
        
            drink_price = returnprice(drink_requested=drink)
        
            #check transaction
        
            if sum_input<drink_price:
                print ("Sorry, that's not enough money. Money refunded")
        
            else: 
                money = money + drink_price
                remaining_resource = {key: resources_local[key] - ingredients[key] for key in set(resources_local) & set(ingredients)}
                resources_local = remaining_resource
                if sum_input>drink_price:
                    change = float(sum_input-drink_price)
                    print (f"Your change is ${change}")
                print (f"Here's your {drink} . Enjoy.")
            
        
        
        
    

    
