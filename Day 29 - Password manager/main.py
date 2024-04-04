from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

path = "Day 29 - Password manager\data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
            }
        
        }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title=website, message="One or more fields are left empty. Please fill them in!")
    
    else:  
        
        try: 
            with open (path, "r") as data_file:
                #Read old data
                data = json.load(data_file)
        
        except FileNotFoundError:
            with open (path, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
            #Update old data with new data
            data.update(new_data)
            with open (path, "w") as data_file:
                json.dump(data, data_file, indent=4)
            
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

    

# ---------------------------- SEARCH PASSWORD IN FILE -----------------------------#

def search():
    
    website = website_entry.get()
    
    try: 
        with open (path, "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No data", message="No data file found. Enter some data first for a data file to be created.")
    else:
        if website in data:
            result = data[website]
            password=result["password"]
            email = result['email']
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password} \n Password has been copied to clipboard.")
        else: 
            messagebox.showinfo(title="No entry found.", message="No entry has been found for this search.")
    
            
            




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day 29 - Password manager/logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Username/Email:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries

website_entry = Entry(width=29)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "test@example.com")

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)

#Buttons

add_btn = Button(text="Add", width=42, command=save)
add_btn.grid(column=1, row=4, columnspan=3)

generate_pw_btn = Button(text="Generate Password", command=generate_password)
generate_pw_btn.grid(column=2, row=3)

search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(column=2, row=1)

window.mainloop()