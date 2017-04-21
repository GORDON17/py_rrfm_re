from urllib2 import Request, urlopen
import os, json, gc
from configurations.env_configs import *

def getMonthCount(uri):
	print ("Sending request to:", uri)
	request=Request(uri)
	request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
	data = json.loads(urlopen(request).read())
	return data