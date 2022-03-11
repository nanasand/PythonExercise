import urllib.request
import urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
#address = input('Enter location: ')
address = 'http://py4e-data.dr-chuck.net/comments_1494460.json'
jason = urllib.request.urlopen(address, context=ctx).read()
info = json.loads(jason)
jsonString = json.dumps(info, indent=4)
print(jsonString)
print('user count: ', len(info['comments']))
for item in info['comments']:
    print('count: ', item['count'])
    sum += int(item['count'])

print(sum)
