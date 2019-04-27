import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(uh), 'characters')

info = json.loads(uh)
print('Count: ', len(info))
count = 0
for i in info:
    print(info['count'])
    #count = count + int(i['comments']['count'])
#print('Sum: ', count)
