import turtle
import re
from svg.path import parse_path, Line, CubicBezier

def setup_turtle():
    screen = turtle.Screen()
    screen.setup(400, 400)
    screen.title("Facebook Logo Drawing")
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()
    return screen, t

def draw_path(t, path, scale=10):
    t.pendown()
    for segment in path:
        if isinstance(segment, Line):
            t.goto(segment.end.real * scale, -segment.end.imag * scale)
        elif isinstance(segment, CubicBezier):
            steps = 100
            for i in range(steps + 1):
                point = segment.point(i / steps)
                t.goto(point.real * scale, -point.imag * scale)
    t.penup()

svg_data = """
<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <circle cx="16" cy="16" r="14" fill="url(#paint0_linear_87_7208)"></circle> <path d="M21.2137 20.2816L21.8356 16.3301H17.9452V13.767C17.9452 12.6857 18.4877 11.6311 20.2302 11.6311H22V8.26699C22 8.26699 20.3945 8 18.8603 8C15.6548 8 13.5617 9.89294 13.5617 13.3184V16.3301H10V20.2816H13.5617V29.8345C14.2767 29.944 15.0082 30 15.7534 30C16.4986 30 17.2302 29.944 17.9452 29.8345V20.2816H21.2137Z" fill="white"></path> <defs> <linearGradient id="paint0_linear_87_7208" x1="16" y1="2" x2="16" y2="29.917" gradientUnits="userSpaceOnUse"> <stop stop-color="#18ACFE"></stop> <stop offset="1" stop-color="#0163E0"></stop> </linearGradient> </defs> </g></svg>
"""

circle_data = re.search(r'<circle.+?></circle>', svg_data).group(0)
path_data = re.search(r'<path.+?></path>', svg_data).group(0)

circle = re.search(r'cx="(\d+)" cy="(\d+)" r="(\d+)"', circle_data)
f_path = parse_path(re.search(r'd="([^"]+)"', path_data).group(1))

screen, t = setup_turtle()

# Draw circle
t.penup()
t.goto(0, -140)  # Adjusted for scale
t.pendown()
t.color("#1877F2")  # Facebook blue
t.begin_fill()
t.circle(140)  # Adjusted for scale
t.end_fill()

# Draw 'f' path
t.penup()
t.goto(f_path[0].start.real * 10, -f_path[0].start.imag * 10)
t.color("white")
t.begin_fill()
draw_path(t, f_path)
t.end_fill()

screen.mainloop()