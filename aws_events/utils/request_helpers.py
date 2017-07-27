import json
import urllib


def post_json(url, data):
    request = urllib.request.Request(url, data=json.dumps(data).encode('utf8'),
                                     headers={'Content-Type': 'application/json'})
    response = urllib.request.urlopen(request)
    
    if response.status != 200:
        print(response.read())
        raise Exception('error while making a request')