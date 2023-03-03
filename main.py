from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(10)


def turn_right():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)


def move_backward():
    pen.backward(10)


def turn_left():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)


def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_left)
screen.onkey(fun=clear, key="c")
screen.exitonclick()
