import turtle
import sys
sys.path.append('../Utils/')
from getColor import getColor as gc

def makeStar():
    t = turtle.Pen()
    t.pensize(10)
    t.penup()
    t.goto(-250,-250)
    t.pendown()
    for i in range(4):
        t.forward(500)
        t.left(90)

    t.penup()
    t.goto(-100,50)
    t.pendown()

    while(1):
        t.begin_fill()
        for i in range(8):
            t.color(gc())
            t.forward(200)
            t.left(225)
        
        t.color(gc(), gc())
        t.end_fill()

makeStar()
