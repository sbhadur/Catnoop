import turtle
import sys
sys.path.append('../Utils/')
from getDirect import getDirect as gd 
from getColor import getColor as gc

map_direct = {
    "up": 90,
    "down": 270,
    "left": 225,
    "right": 135
}

def direct_shape():

    t = []
    for i in range(0,2):
        temp = turtle.Pen()
        temp.penup()
        temp.pensize(4)
        temp.speed(0)
        if i == 0:
            temp.setpos(-250, 0)
        else:
            temp.setpos(250, 0)
        temp.pendown()
        t.append(temp)
    
    while(1):
        for pen in t:
            direct = gd(10)
            pen.color(gc())
            pen.left(map_direct[direct[0]])
            pen.forward(100)


direct_shape()

    