import random
userinput = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
userinput = int(userinput)
computerchoice = random.randint(0, 2)
print (computerchoice)
if userinput == computerchoice:
    print ("It's a tie")
if computerchoice == 0 and userinput == 1:
    print ("Computer chose Rock. You win.")
if computerchoice == 1 and userinput == 2:
    print ("Computer chose Paper. You win.")
if computerchoice == 0 and userinput == 2:
    print ("Computer chose Rock. You lose.")
if computerchoice == 1 and userinput == 0:
    print ("Computer chose Paper. You lose.")
if computerchoice == 2 and userinput == 1:
    print ("Computer chose Scissors. You lose.")
if computerchoice == 2 and userinput == 0: 
    print("Computer chose Scissors. You win")
