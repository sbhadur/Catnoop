import json
import requests

def getColor(count = 0):
    api_base = 'http://api.noopschallenge.com/hexbot'
    if count != 0:
        api_base += '?count=' + str(count)
    response = requests.get(api_base)
    if (response.status_code == 200): 
        response = requests.get(api_base).content.decode('utf-8')
        colors = json.loads(response)['colors']
        if count != 0:
            color_set = []
            for col in colors:
                color_set.append(col['value'])
            return color_set
        return colors[0]['value']
    else:
        return '#FFFFFF'
   

def getColorCoord(width, height):
    api_base = 'http://api.noopschallenge.com/hexbot?width=' + str(width) + '&height=' + str(height)
    response = requests.get(api_base)
    if response.status_code == 200:
        response = requests.get(api_base).content.decode('utf-8')
        colors = json.loads(response)['colors']
        color_coord = []
        color_coord.append(colors[0]['value'])
        color_coord.append(colors[0]['coordinates']['x'])
        color_coord.append(colors[0]['coordinates']['y'])
        return color_coord
    else:
        color_coord = {'#FFFFFF' , 250, 250}
        return color_coord
   


