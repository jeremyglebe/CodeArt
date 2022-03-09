import turtle
from browser import document, window

TURTLE_DIV = document['turtle']
WIDTH = TURTLE_DIV.offsetWidth - 5
HEIGHT = TURTLE_DIV.offsetHeight - 5
MAX_POLYGON = 50
SIDE_LENGTH = 40

turtle._CFG["canvwidth"] = WIDTH
turtle._CFG["canvheight"] = HEIGHT
turtle.set_defaults(
    turtle_canvas_wrapper=TURTLE_DIV
)

tim = turtle.Turtle('turtle')
tim.speed(10)
tim.width(5)
tim.fillcolor('green')
tim.pencolor('black')

tim.penup()
tim.right(90)
tim.goto(-SIDE_LENGTH/2, -.5 * HEIGHT)
tim.left(90)
tim.pendown()

for sides in range(3, MAX_POLYGON):
    for _ in range(sides):
        tim.forward(SIDE_LENGTH)
        tim.left(360/sides)

tim.penup()
tim.forward(SIDE_LENGTH/2)
tim.left(90)
tim.forward(SIDE_LENGTH/4)

turtle.done()
