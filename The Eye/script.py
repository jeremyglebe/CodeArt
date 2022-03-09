import turtle
from browser import document, window

TURTLE_DIV = document['turtle']
WIDTH = TURTLE_DIV.offsetWidth - 5
HEIGHT = TURTLE_DIV.offsetHeight - 5
CIRCLE_RADIUS = 100
DEGREES_PER = 15
ITERATIONS = int(360 / DEGREES_PER)

turtle._CFG["canvwidth"] = WIDTH
turtle._CFG["canvheight"] = HEIGHT
turtle.set_defaults(
    turtle_canvas_wrapper=TURTLE_DIV
)

tim = turtle.Turtle('turtle')
tim.speed(10)
tim.width(5)
tim.fillcolor('green')
tim.pencolor('forestgreen')

# Create circles
for _ in range(ITERATIONS):
    tim.circle(CIRCLE_RADIUS)
    tim.left(DEGREES_PER)

tim.pencolor('black')
# Create circles
for _ in range(ITERATIONS):
    tim.circle(CIRCLE_RADIUS/2)
    tim.left(DEGREES_PER)

# Face up
tim.penup()
tim.right(90)
tim.forward(230)
tim.left(180)

turtle.done()
