import turtle
import sys
sys.path.append('../Utils/')
from getColor import getColorCoord as gcc

def face_gen():
    t = turtle.Pen()
    t.pensize(5)
    t.penup()
    t.goto(-250, -250)
    t.color('black')
    t.pendown()

    for i in range(4):
        t.forward(500)
        t.left(90)

    t.speed(0)
    while(1):
        color_coord = gcc(500, 500)
        t.color(color_coord[0])
        t.penup()
        t.goto(color_coord[1]-250, color_coord[2]-250)
        t.pendown()
        t.goto(color_coord[1]-250, color_coord[2]-250)

face_gen()
