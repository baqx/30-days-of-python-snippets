import turtle

def configure_pen(pen, pcolor, psize, x, y):
    pen.color(pcolor)
    pen.pensize(psize)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

def draw_cnn(pen, initial_step, last_step):
    pen.setheading(180)
    pen.forward(initial_step)
    pen.circle(50, 180)
    pen.forward(50)
    pen.left(90)
    pen.forward(95)
    for _ in range(2):
        pen.circle(-5, 150)
        pen.forward(110)
        pen.circle(5, 180)
        pen.setheading(90)
        pen.forward(85)
    pen.forward(last_step)

pen, screen= turtle.Turtle(), turtle.Screen()
pen.hideturtle()

configure_pen(pen, "#cc0000", 30, -55, 50)
screen.bgcolor("#ffffff")
draw_cnn(pen, 15, 5)
configure_pen(pen, "#ffffff", 5, -41, 50)
draw_cnn(pen, 29, 20)
screen.exitonclick()