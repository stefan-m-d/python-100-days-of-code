import random
print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
number_to_guess = random.choice(range(1,101))
#DEBUG ONLY - print (f"Psst. The number is {number_to_guess}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts_left = 0
if difficulty == "easy":
    attempts_left = 10
else: 
    attempts_left = 5
print(f"You have {attempts_left} attempts left to guess the number.")

def guess(number):
    Guess_flag = True
    if number<number_to_guess:
        print ("Too low.")
        Guess_flag = False
        return Guess_flag
    elif number>number_to_guess:
        print ("Too high.")
        Guess_flag = False
        return Guess_flag
    else:
        print (f"You got it! The number was {number}")
        return Guess_flag

flag = True
while flag:
    user_input = int(input("Make a guess: "))
    Number_Guessed_Flag=guess(number=user_input)
    attempts_left -= 1
    if Number_Guessed_Flag == True:
         exit()
    elif attempts_left != 0:
        print(f"Guess again. \nYou have {attempts_left} attempts remaining to guess the number. \n")
    else: 
        flag = False
        print (f"You've run out of guesses. You lose. The number was {number_to_guess}")
        


# SOLUTION CODE PROVIDED IN THE VIDEO
# from random import randint
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
# def check_answer(guess, answer, turns):
#   if guess > answer:
#       print ("Too high.")
#       return turns - 1
#   elif guess < answer:
#       print ("Too low.")
#       return turns - 1 
#   else: 
#       print(f"You got it! The answer was {answer}.")
#
# def set difficulty():
#   level = input ("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#       return EASY_LEVEL_TURNS
#   else:
#       return HARD_LEVEL_TURNS
# def game():
#   print ("Welcome to the Number Guessing Game!")
#   print ("I'm thinking of a number between 1 and 100.")
#   answer = randint(1,100)
#   print (f"Psst. The answer is {answer}")
#   
#   turns = set_difficulty() 
#   guess = 0
#   while guess != answer:
#       print (f"You have {turns} attemprs remaining to guess the number.")
#
#       guess = int(input("Make a guess: "))
#   
#       turns = check_answer(guess, answer, turns)
#
#       if turns == 0:
#           print("You've run out of guesses. You lose.")
#           return
#       elif guess !=answer: 
#           print ("Guess again.")
#
#
#
# game()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#