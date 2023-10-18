import random
letternumber = input ("Welcome to PyPassword Generator. \n How many letters would you like in your password? \n")
letternumber = int(letternumber)
symbolsnumber = input ("How many symbols would you like? \n")
symbolsnumber = int(symbolsnumber)
numbersnumber = input ("How many numbers would you like? \n")
numbersnumber = int(numbersnumber)
passwordstring = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['@', '!', '#', '$', '%', '*', '&']
for char in range(1, letternumber+1):
    passwordstring.append(random.choice(letters))
for char in range (1, numbersnumber+1):
    passwordstring.append(random.choice(numbers))
for char in range (1, symbolsnumber+1):
    passwordstring.append(random.choice(symbols))
random.shuffle(passwordstring)
password=""
for char in passwordstring:
    password+=char
print ("Your password is " + password)