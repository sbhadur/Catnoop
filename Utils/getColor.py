import json
import requests

def getColor():
    api_base = 'http://api.noopschallenge.com/hexbot'
    response = requests.get(api_base).content.decode('utf-8')
    colors = json.loads(response)['colors']
    return colors[0]['value']
    
