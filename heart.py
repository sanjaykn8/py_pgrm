import turtle
import time

pen = turtle.Turtle()

def curve():
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
    
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    
heart()
time.sleep(3)
turtle.done
