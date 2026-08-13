import urllib.request, urllib.parse, urllib.error
import json
sertviceurl = 'https://py4e-data.dr-chuck.net/opengeo?q=AGH+University+of+Science+and+Technology'
while True:
    address = input('enter location: ')
    if len(address) < 1: break
    url = sertviceurl + urllib.parse.urlencode({'address': address})
    # print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    # print(len(data))
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'ok':
        # print('Failure')
        # print(data)
        continue
    lat = js['result'][0]['geometry']['location']['lat']
    lng = js['result'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['result'][0]['formattef_address']
    print(location)