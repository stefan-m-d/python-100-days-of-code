print ("Welcome to Treasure Island")
print ("Your mission is to find the treasure.")
direction = input("""You're at a crossroad. Where do you want to go? Type "left" or "right"?""")
if "right" in direction:
    print ("You fell into a hole. Game over.")
    exit ()

action = input("""You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across """)
if "swim" in action: 
        print ("You get attacked by an angry trout. Game over.")
        exit ()
        
door = input ("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
if "red" in door: 
            print ("It's a room full of fire. Game over")
if "yellow" in door: 
            print ("You found the treasure! You win!")
if "blue" in door: 
            print ("You enter a room full of beasts. Game over.")
