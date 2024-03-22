import pandas

df = pandas.read_csv("Day 26 - NATO phonetic alphabet and list and dict comprehension/nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input ("Please enter a word or a name: ")
capitalized = [char.capitalize() for char in user_input]

otan_list = [dict[char] for char in capitalized]

print (otan_list)