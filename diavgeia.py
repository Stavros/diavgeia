#Diavgeia API parser example - diavgeia.py - Stavros Kalapothas

import urllib.request
import json

size = int(input('Enter number of decisions: '))
url = 'https://diavgeia.gov.gr/luminapi/opendata/search.json?&size={}'.format(size) # build url incl. parameter

req = urllib.request.Request(url)
response = urllib.request.urlopen(req,timeout=90000)
the_page = response.read() # bytes
doc=the_page.decode("utf-8") # convert to string
doc=json.loads(doc) # convert to dictionary
#print(doc)    #debug

count = 0   # simple counter

for apofasi in doc['decisions']:
    count +=1
    print('\n',count, apofasi['subject'])   # return value from subject
