import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day 25 - CSV Data and the Pandas library/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pandas.read_csv("Day 25 - CSV Data and the Pandas library/50_states.csv")

all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    screen.title(f"U.S. States Game {len(guessed_states)} / 50")
    answer_state = screen.textinput(title = f"{len(guessed_states)}/ 50 States Correct", prompt = "Name a state").title()
    if answer_state == "Exit":
        states_to_learn = []

        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)

        new_df = pandas.DataFrame(states_to_learn)
        new_df.to_csv("Day 25 - CSV Data and the Pandas library/states_to_learn.csv")
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# states_to_learn.csv

