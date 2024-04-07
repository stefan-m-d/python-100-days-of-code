from tkinter import *
import os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = ""

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Update the image paths with the correct relative paths
RIGHT_IMAGE_PATH = os.path.join(current_dir, "images", "right.png")
WRONG_IMAGE_PATH = os.path.join(current_dir, "images", "wrong.png")
CARD_FRONT_PATH = os.path.join(current_dir, "images", "card_front.png")
CARD_BACK_PATH = os.path.join(current_dir, "images", "card_back.png")
DEFAULT_CSV_PATH = os.path.join(current_dir, "data", "french_words.csv")
WORDS_TO_LEARN_CSV_PATH = os.path.join(current_dir, "data", "words_to_learn.csv")

#get CSV with pandas

try: 
    df = pandas.read_csv(WORDS_TO_LEARN_CSV_PATH)
except FileNotFoundError:
    print("File not found. Loading default file")
    df = pandas.read_csv(DEFAULT_CSV_PATH)
finally: 
    to_learn = df.to_dict(orient="records")

def remove_card():
    to_learn.remove(current_card)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(french_word, text=current_card["French"], fill="black")
    canvas.itemconfig(Language, text="French", fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
    
    
def flip_card():
    canvas.itemconfig(Language, text="English", fill="white")
    canvas.itemconfig(french_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)

def save_remaining_cards():
    new_data = pandas.DataFrame.from_dict(to_learn)
    new_data.to_csv(WORDS_TO_LEARN_CSV_PATH, index=False)

#window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#images
card_front_img = PhotoImage(file=CARD_FRONT_PATH)
card_back_img=PhotoImage(file=CARD_BACK_PATH)
right_img=PhotoImage(file=RIGHT_IMAGE_PATH)
wrong_img=PhotoImage(file=WRONG_IMAGE_PATH)

#canvas

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_bg = canvas.create_image(0, 0,anchor=NW , image=card_front_img)
canvas.grid(column=0, row=1, columnspan=2)

#buttons

right_btn = Button(image=right_img, highlightthickness=0, command=remove_card)
right_btn.grid(column=0, row=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=1, row=2)

#labels

Language = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 263, text="Test", font=("Ariel", 60, "bold"))
next_card()

window.mainloop()

save_remaining_cards()