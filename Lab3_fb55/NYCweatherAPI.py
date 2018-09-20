from __future__ import print_function
import json
import urllib2 
import os
import sys


apikey = os.getenv("WEATHERAPIKEY")
mode = "Json"
units = "metric"
city = sys.argv[1]

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&mode=%s&units=%s&cnt=7&APPID=%s"%(city, mode, units, apikey)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
print (dataDict)
