import turtle
import sys
sys.path.append('../Utils/')
from getColor import getColorCoord as gcc

def face_gen():
    t = turtle.Pen()
    t.speed(3)
    t.pensize(5)
    t.penup()
    t.goto(-250, -250)
    t.color('black')
    t.pendown()
    

    for i in range(4):
        t.forward(500)
        t.left(90)

    penSize = 1
    t.speed(0)
    increasing = True
    while(1):
        t.pensize(penSize)
        t.speed(penSize)
        color_coord = gcc(500, 500)
        t.color(color_coord[0])
        t.goto(color_coord[1]-250, color_coord[2]-250)

        if not increasing:
            penSize -= 1
            if penSize == 1:
                increasing = True
        if increasing:
            penSize += 1
            if penSize == 10:
                increasing = False

face_gen()