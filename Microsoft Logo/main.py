import turtle

def draw_spotify(pen):
    """ Draw the Spotify logo with a green theme. """
    # Set properties and initial position.
    pen.hideturtle()
    pen.speed("fast")
    pen.penup()
    pen.goto(-160, -90)
    pen.pendown()
    pen.showturtle()

    # Draw the circle.
    pen.color("#1db954")
    pen.begin_fill()
    pen.circle(90)
    pen.end_fill()

    # Draw the bottom curve.
    pen.penup()
    pen.goto(-120, -40)
    pen.pencolor("#ffffff")
    pen.left(140)
    pen.pendown()
    pen.pensize(10)
    pen.circle(90, 60)

    # Draw the middle curve.
    pen.penup()
    pen.goto(-110, -20)
    pen.right(60)
    pen.pendown()
    pen.pensize(12)
    pen.circle(105, 60)

    # Draw the top curve.
    pen.penup()
    pen.goto(-100, 5)
    pen.right(60)
    pen.pendown()
    pen.pensize(15)
    pen.circle(120, 60)

    # Set text color and write "Spotify".
    pen.penup()
    pen.goto(-40, -60)
    pen.color("#1db954")
    pen.pendown()
    pen.write("Spotify", font=("Arial", 70, "bold"))
    pen.hideturtle()

# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set background color.
screen.bgcolor("#000000")

# Draw logo.
draw_spotify(pen)

# Hold screen.
screen.exitonclick()
