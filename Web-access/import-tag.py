import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sum = sum + int(tag.text)
print(sum)
