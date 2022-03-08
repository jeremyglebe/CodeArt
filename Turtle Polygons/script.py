from browser import document, window
import turtle
turtle._CFG["canvwidth"] = window.innerWidth
turtle._CFG["canvheight"] = window.innerHeight
turtle.set_defaults(
    turtle_canvas_wrapper=document['turtle']
)

MAX_POLYGON = 50

tim = turtle.Turtle('turtle')
tim.speed(10)
tim.width(5)

tim.penup()
tim.goto(0, -.5 * window.innerHeight)
tim.pendown()

for sides in range(3, MAX_POLYGON):
    for _ in range(sides):
        tim.forward(40)
        tim.left(360/sides)

turtle.done()
