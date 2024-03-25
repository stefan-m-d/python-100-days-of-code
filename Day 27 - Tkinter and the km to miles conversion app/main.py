from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

button_label = Label(text= "Unga bunga computing", font=("Arial", 29, "bold"))

conversion = 1.609344

input = Entry(width=10)
input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 24))
miles_label.grid(column=3, row=1)

is_equal_to_label = Label(text="Is equal to ", font=("Arial", 24))
is_equal_to_label.grid(column=1, row=2)

kilometres_label = Label(text="Km", font=("Arial", 24))
kilometres_label.grid(column=3, row=2)

answer_label = Label(font=("Arial", 24))
answer_label.grid(column=2, row=2)

def button_clicked():
    miles = int(input.get())
    miles *= conversion
    miles = round(miles, 2)
    answer_label.config(text=miles)

button = Button(text = "Convert", command=button_clicked, font=("Arial", 24, "bold"))
button.grid(column=2, row=3)





window.mainloop()

