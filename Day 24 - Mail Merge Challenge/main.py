import os

main_file_path = os.path.dirname(os.path.abspath(__file__))
invited_names_file_path = "D:/python course code and others/Day 24 - Mail Merge Challenge/Input/Names/invited_names.txt"
starting_letter_file_path = "D:/python course code and others/Day 24 - Mail Merge Challenge/Input/Letters/starting_letter.txt"
letter_save_path = "D:/python course code and others/Day 24 - Mail Merge Challenge/Output/ReadyToSend/"

names = []
letter_template = ""

# open invited names and get them as var

with open(invited_names_file_path) as file:
    for line in file:
        row = line.rstrip('\n')
        names.append(row)

# get the letter template

with open(starting_letter_file_path) as file:
    letter_template = file.read()

for name in names:
    
    #replace [name] in the letter template with the name in the list
    letter_name = letter_template.replace("[name]", name)
    
    #this is the new file name
    name_of_file = name+".txt"
    
    #open this file and create it if it does not exist
    f = open(os.path.join(letter_save_path, name_of_file), "w")
    
    f.write(letter_name)
    f.close()