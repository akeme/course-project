# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_1551447.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum = 0

# Retrieve all of the anchor tags
spans = soup('span')
for span in spans:
    # Look at the parts of a tag
    print('TAG:', span)
    # print('URL:', tag.get('href', None))
    print('Contents:', span.contents[0])
    sum += int(span.contents[0])
    # print('Attrs:', tag.attrs)

print("Total: ", sum)