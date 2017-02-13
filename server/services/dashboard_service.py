from urllib2 import Request, urlopen
import os, json, gc

def getMonthCount(uri):
	print ("Sending request to:", uri)
	request=Request(uri)
	data = json.loads(urlopen(request).read())
	return data