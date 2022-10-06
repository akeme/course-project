# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = " http://py4e-data.dr-chuck.net/known_by_Zaynab.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#question
num_times = 6
num_position = 17 
times = 0

# Retrieve all of the anchor tags
tags = soup('a')

while times <= num_times:
    for idx, tag in enumerate(tags):
        print(idx, tag.get('href', None))
        if idx == num_position:
            url = tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            print(tag.get('href', None))
            tags = soup('a')
            times += 1
            print(times)
            break





