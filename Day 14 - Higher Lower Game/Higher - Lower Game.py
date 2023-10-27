#Higher - Lower Game

import random

#existing file obtained from replit for the game

import game_data

def game():
    
    # get 2 random dictionaries from the list of dictionaries in the game data

    A = random.choice(game_data.data)
    B = random.choice(game_data.data)
    
    #set a flag to determine whether to keep playing
    game_over = False 
    
    #set a var for score
    score = 0
    
    #Set a new B if it's the same follower count as A
    
    if A['follower_count']==B['follower_count']:
        
        B = random.choice(game_data.data)
    
    print ("Welcome to the guessing game.")
    
    #Start game
    
    while game_over !=True: 
        
        #DEBUG ONLY - PRINT FOLLOWER COUNT
        # print ("A's follower count is "+ str(A['follower_count'])+" and B's follower count is "+str(B['follower_count'])) 
        user_input = input("Compare A: "+A['name']+" , a "+ A['description']+" from "+ A['country']+"  \n\n"+ "With B: "+B['name']+" , a "+ B['description']+" from "+ B['country']+"\n Type A or B: ")
        
        #happy path
    
        if user_input.lower() == "a" and A['follower_count']>B['follower_count']:
            
            A=B
        
            B = random.choice(game_data.data)
            
            score = score+1
            
            if A['follower_count']==B['follower_count']:
        
                B = random.choice(game_data.data)
            
            print (f"You got it. Your score is {score}\n")
        
        #happy path
        
        elif user_input.lower() == "b" and B['follower_count']>A['follower_count']:
            
            A=B
        
            B = random.choice(game_data.data)
                        
            if A['follower_count']==B['follower_count']:
        
                B = random.choice(game_data.data)
            
            score = score+1
            
            print (f"You got it. Your score is {score}\n")
            
        #game over    
        
        else: 
            
            game_over = True 
            
            print (f"Sorry, you lose. Your score is {score}")
    
game ()    