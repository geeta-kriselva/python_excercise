import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#defining class to extract html files
def html(url, count, pos):
    for i in range(1, count+1):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")

        tags = soup('a')
        url = tags[pos-1].get(('href', None))
        print(url)
        # hreflist = []
        # cnt = 0
        # for tag in tags:
        #     if cnt < pos:
        #         hreflist.append([tag.get('href', None)])
        #     else:
        #         url = hreflist[pos][0]
        #         break
        #     cnt = cnt + 1
        #     print(url)
        #     print(cnt)
    return url


#opening first file
url = input('Enter the url: ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

x = html(url, count, pos)
