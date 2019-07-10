import json
import requests

def getDirect(maxSpeed):
    api_base = 'http://api.noopschallenge.com/directbot'
    if(maxSpeed):
        api_base = 'http://api.noopschallenge.com/directbot?speed=' + str(maxSpeed)
    response = requests.get(api_base)
    if response.status_code == 200:
        response = requests.get(api_base).content.decode('utf-8')
        direct = json.loads(response)['directions']
        direct_stats = []
        direct_stats.append(direct[0]['direction'])
        direct_stats.append(direct[0]['distance'])
        direct_stats.append(direct[0]['speed'])
        return direct_stats
    direct_stats = {"left", 25, 0}
    return direct_stats
   
