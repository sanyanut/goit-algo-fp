import turtle
import math


def pythagoras_tree(t, order, size, angle):
    if order == 0:
        return

    t.forward(size)

    t.left(angle)
    pythagoras_tree(t, order - 1, size / math.sqrt(2), angle)

    t.right(2 * angle)
    pythagoras_tree(t, order - 1, size / math.sqrt(2), angle)

    t.left(angle)
    t.backward(size)


size = 150
angle = 45

order = int(input("Enter a number of recursion: 5-10: "))

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("red")
t.speed(500)
t.left(90)
t.goto(0, -150)

pythagoras_tree(t, order, size, angle)

turtle.done()
