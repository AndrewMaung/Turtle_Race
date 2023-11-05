from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet!", prompt="Which color will win the race,enter your color(red,blue,green,orange,yellow,purple): ").lower()
color_list = ["red", "blue", "green", "purple", "orange", "yellow"]
y_coordinates = [-100, -60, -20, 20, 60, 100]
all_turtle = []

if user_input:
    is_race_on = True

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[turtle_index])
    all_turtle.append(new_turtle)

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_input == winning_color:
                print(f"You won! The winning color is {winning_color}")
            else:
                print(f"You lost! The winning color is {winning_color}")
            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
