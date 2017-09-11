from urllib2 import Request, urlopen
import os, json, gc
from configurations.env_configs import *
from services.api_service import *

def getMonthCount(uri):
	return APIService().get_request(uri, 500)