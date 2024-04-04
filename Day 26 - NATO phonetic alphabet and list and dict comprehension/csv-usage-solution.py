import pandas

df = pandas.read_csv("Day 26 - NATO phonetic alphabet and list and dict comprehension/nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    user_input = input ("Please enter a word or a name: ").upper()
    try: 
        otan_list = [dict[char] for char in user_input]

    except KeyError:
        print ("Invalid input. Letters only, please.")
        generate_phonetic()
    else:
        print (otan_list)
    
generate_phonetic()