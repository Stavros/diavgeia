#Futurium API parser example - futurium.py - Stavros Kalapothas

import urllib.request
import json

size = int(input('Enter number: '))
url = ''.format(size) # build url incl. parameter

req = urllib.request.Request(url)
response = urllib.request.urlopen(req,timeout=90000)
the_page = response.read() # bytes
doc=the_page.decode("utf-8") # convert to string
doc=json.loads(doc) # convert to dictionary
#print(doc)    #debug

count = 0   # simple counter

for item in doc['comments']:
    print('\n',count, item['comment']) # return value from subject
    count +=1