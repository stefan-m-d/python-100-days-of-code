import random
life = 6
life = int(life)
wordslibrary = ["boom", "airplane", "aircraft", "pilot", "beekeeper" ]
word = random.choice(wordslibrary)
wordtoguess = []
for char in word: 
    wordtoguess.append("_")
print(''.join(wordtoguess))
index = 0
indices = []
userinput = input ("Welcome to the hangman game. Please input a letter. \n")
while life !=0: 
    if userinput in word:
        count = word.count(userinput)
        if count > 1:
            indices = [ index for (index, item) in enumerate(word) if item ==userinput]
            for i in indices:
                index = i
                wordtoguess[index] = userinput
            print(''.join(wordtoguess))
        else: 
            index = word.index(userinput)
            wordtoguess[index] = userinput
            print(''.join(wordtoguess))
    else: 
        life=life-1
        print ("No "+str(userinput)+" in word. Remaining life:" + str(life))
    if "_" not in wordtoguess: break
    userinput = input("Please enter a letter \n")
if "_" not in wordtoguess and life!=0:
    print ("Congrats. You guessed the word - " + str(word))
else: 
    print ("You lost. The word was " + str(word))