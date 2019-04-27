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

count = 0
commentlist = info.get("comments")
print("Count: ", len(commentlist))
for i in commentlist:
    count = count + i["count"]
print("Sum: ", count)
