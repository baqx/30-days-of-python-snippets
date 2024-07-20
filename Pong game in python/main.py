import turtle
win = turtle.Screen()
win.bgcolor('black')
paddle = turtle.Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=6, stretch_len=1)
def paddle_up():
    y = paddle.ycor()
    y += 20
    paddle.sety(y)
win.listen()
win.onkey(paddle_up, 'Up')
while True:
    win.update()
