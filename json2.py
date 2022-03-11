import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #address = input('Enter location: ')
    #address = 'South Federal University'
    address = 'allama iqbal open university islamabad'
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    jsonString = json.dumps(js, indent=4)
    print(jsonString)

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    loc = js['results'][0]['place_id']
    print('latitude :', lat)
    print('longitude :', lng)
    print('place_id', loc)
