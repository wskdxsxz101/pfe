import urllib.error, urllib.parse, urllib.request
import json
sertviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
while True:
    address = input("enter:")
    if len(address) < 1: break

    url = sertviceurl + urllib.parse.urlencode({'q' : address})
    print('e_address:', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        print('fall to exchange')
        continue

    if not js or not 'features' in js or len(js) == 0:
        print('no features')
        print(data)
        break

    lon = js['features'][0]['properties']["lon"]
    lat = js['features'][0]['properties']["lat"]
    print(lon, lat)
    
    
