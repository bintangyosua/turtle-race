import turtle
import random


is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Nake your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

timmy = turtle.Turtle(shape="turtle")
temmy = turtle.Turtle(shape="turtle")
tommy = turtle.Turtle(shape="turtle")
johnny = turtle.Turtle(shape="turtle")
jennie = turtle.Turtle(shape="turtle")
jamie = turtle.Turtle(shape="turtle")


turtles = [timmy, temmy, tommy, johnny, jennie, jamie]
some_y = -75

for turtle_index in range(0, 6):
    turtles[turtle_index].color(colors[turtle_index])
    turtles[turtle_index].penup()
    turtles[turtle_index].goto(x=-230, y=some_y)
    some_y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(10, 30)
        turtle.forward(rand_distance)

screen.exitonclick()
