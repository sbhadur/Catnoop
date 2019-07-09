import json
import requests
import turtle
import tkinter
import random

def getColor():

    t = turtle.Pen()
    t.pensize(10)

    while(1):
        t.begin_fill()
        for i in range(8):
            api_base = 'http://api.noopschallenge.com/hexbot'
            response = requests.get(api_base).content.decode('utf-8')
            colors = json.loads(response)['colors']
            t.color(colors[0]['value'])
            t.forward(200)
            t.left(225)
        
        api_base = 'http://api.noopschallenge.com/hexbot'
        response = requests.get(api_base).content.decode('utf-8')
        colors = json.loads(response)['colors']
        t.color(colors[0]['value'], colors[0]['value'])
        t.end_fill()

getColor()
