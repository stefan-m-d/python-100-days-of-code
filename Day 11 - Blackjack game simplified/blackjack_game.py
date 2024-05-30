#code I previously came up with
"""import random
allcards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playercards = []
computercards = []
cardamount=0
playerscore=0
computerscore=0
playerloss=False
computerloss=False
def initialdeal():
    global playercards
    global computercards
    for char in range (1,3):
        playercards.append(random.choice(allcards))
        computercards.append(random.choice(allcards))
    print (f"Your cards: {playercards}")
    print (f"Computer's first card: {computercards[0]}")
        
def checkwin():
    global cardamount
    cardamount = sum(playercards)
    if cardamount == 21:
            print ("You win.")
            exit()
    else:
        cardamount=0
        cardamount = sum(computercards)
        if cardamount == 21:
            print (f"You lose. Computer won with {computercards} ")
            exit()
        else: 
            cardamount=0
            
def bust():
    global cardamount
    global playerloss
    global computerloss
    global playerscore
    global computerscore
    cardamount = sum(playercards)
    playerscore=cardamount
    if cardamount>21: 
        playerloss = True
        return playerloss
    else:
        cardamount=0
        cardamount = sum(computercards)
        computerscore=cardamount
        if cardamount > 21:
            computerloss = True
            return computerloss
        else: 
            cardamount=0
            
def getplayeramount():
    global cardamount
    global playerscore
    cardamount = sum(playercards)
    playerscore=cardamount
    cardamount=0

def getcomputeramount():
    global cardamount
    global computerscore
    cardamount = sum(computercards)
    computerscore=cardamount
    cardamount=0

def computerlogic():
    global computerscore
    global playerscore
    getplayeramount()
    getcomputeramount()
    if computerscore>playerscore:
        print (f"You lose. Computer has {computerscore} which is greater than your {playerscore}")
    elif computerscore<16:
        computercards.append(random.choice(allcards))

def init():
    global playerscore
    global playercards
    global playerloss
    global computercards
    global computerloss
    global computerscore
    playerscore=0
    computerscore=0
    playercards = []
    computercards = []
    playerloss = False
    computerloss = False

flag = True
addcardflag=True
while flag: 
    gameon = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if gameon =='n':
        flag = False
        break
    else:
            init()
            initialdeal()
            checkwin()
            while addcardflag:
                add_card = input("Type 'y' to get another card. Type 'n' to pass: ")
                if add_card == 'y':
                    playercards.append(random.choice(allcards))
                    print (f"Your cards are {playercards}")
                    checkwin()
                    bust()
                    if playerloss == True: 
                        print (f"You lose. Your score is {playerscore}")
                        addcardflag = False
                else: 
                    addcardflag = False
                    getplayeramount()
            if playerloss == False:
                computerlogic()
                checkwin()
                bust()
                if computerloss == True:
                    print (f"You win. Computer busted with score {computerscore}")
                else: 
                    getplayeramount()
                    getcomputeramount()
                    if playerscore>computerscore:
                        print (f"You win with {playerscore} to computer's {computerscore}")
                    else:
                        print (f"Computer wins with {computerscore} to your {playerscore}")
            addcardflag=True
            
        
"""
#solution:

import random 
import os
def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card

def calculate_score(cards):
   if sum(cards) == 21 and len(cards) == 2:
       return 0
   if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)
def compare(user_score, computer_score):
   if user_score == computer_score:
       return "Draw"
   elif computer_score==0:
       return "You lose. Your opponent has Blackjack"
   elif user_score==0:
       return "You win. You have a Blackjack"
   elif user_score>21:
       return "You went over. You lose"
   elif computer_score>21:
       return "Computer went over. You win"
   elif user_score>computer_score:
       return "You win."
   else:
       return "You lose."

def play_game():
   user_cards=[]
   computer_cards=[]
   is_game_over = False 
   for _ in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())
   while not is_game_over:
       user_score = calculate_score(user_cards)
       computer_score = calculate_score(computer_cards)
       print (f"Your cards: {user_cards}, current score: {user_score}")
       print (f"Computer's first card: {computer_cards[0]}")
       if user_score == 0 or computer_score == 0 or user_score > 21:
           is_game_over = True
       else:
           user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
       if user_should_deal =="y":
           user_cards.append(deal_card())
       else:
           is_game_over = True

   while computer_score!=0 and computer_score<17:
       computer_cards.append(deal_card())
       computer_score = calculate_score(computer_cards)

   print(f"Your final hand: {user_cards}, final score: {user_score}")
   print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
   print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")== 'y':
   os.system('cls')
   play_game()
