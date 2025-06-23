import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "political-map.gif"
turtle.addshape(image)
turtle.shape(image)
instruction_turtle = turtle.Turtle()
instruction_turtle.hideturtle()
instruction_turtle.penup()
instruction_turtle.goto(120, 210)
instruction_turtle.write(
    "* Welcome to the India States & UTs Game!\n"
    "* Type the name of a State or UT and it will appear \n   on the map.\n"
    "* Type 'Exit' or press Cancel to end the game early.",
    align="center", font=("Arial", 8, "bold")
)
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()

data = pandas.read_csv("India States-UTs.csv")
all_states_and_uts = data["State/UT"].to_list()
guess_states_ut = []

while len(guess_states_ut) < 36:
    answer_state = screen.textinput(title=f"{len(guess_states_ut)}/36 States/UT Correct",
                                    prompt="What's another state's name?")

    message_turtle.clear()

    if answer_state is None:
        break

    state_input = answer_state.strip().title()

    if state_input == "Exit":
        missing_states_ut = [state for state in all_states_and_uts if state not in guess_states_ut]
        missed_states_ut = pandas.DataFrame(missing_states_ut)
        missed_states_ut.to_csv("states_you_missed.csv")
        break
    if state_input in all_states_and_uts and state_input not in guess_states_ut:
        guess_states_ut.append(state_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_ut_data = data[data["State/UT"] == state_input]
        t.goto(state_ut_data.x.item(), state_ut_data.y.item())
        t.write(state_input)
    elif state_input in guess_states_ut:
        message_turtle.clear()
        message_turtle.goto(0, -260)
        message_turtle.write(f"You already guessed {state_input}. Try Another.",
                             align="center", font=("Arial", 12, "normal"))


score = len(guess_states_ut)
message_turtle.clear()
message_turtle.goto(0, -280)
message_turtle.write(f"Game Over! You guessed {score} out of 36 states/UTs.",
                     align="center", font=("Arial", 14, "bold"))


turtle.exitonclick()