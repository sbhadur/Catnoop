import json
import requests

def getColor():
    api_base = 'http://api.noopschallenge.com/hexbot'
    response = requests.get(api_base).content.decode('utf-8')
    colors = json.loads(response)['colors']
    return colors[0]['value']
   

def getColorCoord(width, height):
    api_base = 'http://api.noopschallenge.com/hexbot?width=' + str(width) + '&height=' + str(height)
    response = requests.get(api_base).content.decode('utf-8')
    colors = json.loads(response)['colors']
    color_coord = []
    color_coord.append(colors[0]['value'])
    color_coord.append(colors[0]['coordinates']['x'])
    color_coord.append(colors[0]['coordinates']['y'])
    return color_coord
   

