from tkinter import *
import math 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1
    
    work_sec=WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text = "Break", fg = PINK)
    else: 
        countdown(work_sec)
        timer_label.config(text = "Work", fg = GREEN)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+=checkmark
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

checkmark="✔"


canvas = Canvas(width=200, height=260, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28 - Pomodoro app/tomato.png")
canvas.create_image(100, 112,image=tomato_img)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start = Button(text = "Start", command=start_timer, bg=YELLOW, font=(FONT_NAME, 25, "bold"), highlightthickness=0)
start.grid(column=1, row=3)

reset = Button(text = "Reset", command=reset_timer, bg=YELLOW, font=(FONT_NAME, 25, "bold"), highlightthickness=0)
reset.grid(column=3, row=3)

checkmark_label = Label(font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


window.mainloop()