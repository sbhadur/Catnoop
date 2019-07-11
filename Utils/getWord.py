import json
import requests

def getWord(count = 0, category = None):
    api_base = "https://api.noopschallenge.com/wordbot?"
    if count != 0:
        api_base += "count=" + str(count) + "&"
    if category != None:
        api_base += "set=" + str(category)
        
    response = requests.get(api_base)
    if (response.status_code == 200): 
        response = requests.get(api_base).content.decode('utf-8')
        response = json.loads(response)
        if count == 0: 
            return response['words'][0]
        
        words = []
        for word in response['words']:
            words.append(word)
        return words


