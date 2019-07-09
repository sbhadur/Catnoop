import turtle
import tkinter
import sys
sys.path.append('../Utils/')
from getColor import getColor as gc

def makeStar():
    t = turtle.Pen()
    t.pensize(10)

    while(1):
        t.begin_fill()
        for i in range(8):
            t.color(gc())
            t.forward(200)
            t.left(225)
        
        t.color(gc(), gc())
        t.end_fill()

makeStar()
