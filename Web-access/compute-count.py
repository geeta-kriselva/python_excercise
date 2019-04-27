import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(uh), 'characters')
tree = ET.fromstring(uh)
commentlist = tree.findall('comments/comment')
print('Count: ', len(commentlist))
print(commentlist)
count = 0
for i in commentlist:
     x = i.find('count').text
     count = count + int(x)
print('Sum: ', count)
