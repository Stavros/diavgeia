#APD Kritis API parser example - apdkritis.py - Stavros Kalapothas

import urllib.request
import json
import datetime

limit = int(input('Enter number of measurements: '))
res_id = 'b7ca9fdb-171a-4a6c-a89d-890e16ebcc23' # real time meteorological dataset
now = datetime.datetime.now().strftime("%Y-%m-%d")
url = 'https://www.apdkritis.gov.gr/el/api/action/datastore/search.json?sort[Time]=desc&resource_id={0}&limit={1}&filter[Date]={2}'.format(res_id, limit, now) # build url incl. parameter

req = urllib.request.Request(url)
response = urllib.request.urlopen(req,timeout=90000)
the_page = response.read() # bytes
doc=the_page.decode("utf-8") # convert to string
doc=json.loads(doc) # convert to dictionary
#print(doc)    #debug

count = 0   # simple counter

for item in doc['result']['records']:
    print('\n',count, now, item['Time'], item['AIR TEMP']) # return value from subject
    count +=1