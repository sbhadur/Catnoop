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
    turtle.bgcolor(gc())
    turtle.title("Direct Bots: Rave Mode")
    
    #Epilepsy checks
    epilepsy = turtle.numinput("WARNING", "Type 1 if you have epilepsy: ", default = 0, minval = 0, maxval = 1)
    if (epilepsy == 1): 
        turtle.bye()

    #Player Select
    playernum = turtle.numinput("Player Select", "First turtle to leave the map wins\n  - Left: 0 \n  - Right: 1", default = 0, minval = 0, maxval = 1)

    r = turtle.Pen()
    makeBox(r)

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
        colors = gc(6)
        for pen in t:
            turtle.bgcolor(colors[0])
            direct = gd(10)
            turtle.bgcolor(colors[1])
            
            pen.color(colors[2])
            turtle.bgcolor(colors[3])
            
            pen.left(map_direct[direct[0]])
            turtle.bgcolor(colors[4])
            
            pen.forward(100)
            turtle.bgcolor(colors[5])
            if (pen.xcor() > 800 or pen.xcor() < -800 or pen.ycor() > 365 or pen.ycor() < -385):
                turtle.clear()
                text = turtle.textinput("Game Over", "Please leave now: ")
                if (text == "No"):
                    direct_shape()
                else:
                    turtle.bye()
                    return
            

def makeBox(r):
    r.pensize(10)
    r.penup()
    r.goto(-800,-385)
    r.pendown()
    r.forward(1600)
    r.left(90)
    r.forward(750)
    r.left(90)
    r.forward(1600)
    r.left(90)
    r.forward(750)

direct_shape()

 
