# Graphich Seven Star Ring
import turtle
win = turtle.Screen()
win.bgcolor("white")
z = turtle.Turtle()
for i in range(35):
    z.color("blue")
    z.forward((80))
    z.right(144)

    z.color("red")
    z.forward((80))
    z.right(144)

    z.color("black")
    z.forward((80))
    z.right(144)

    z.color("orange")
    z.forward((80))
    z.right(144)

    z.color("green")
    z.forward((80))
    z.right(144)
    
    z.right(50)
    z.forward(100)

turtle.done()