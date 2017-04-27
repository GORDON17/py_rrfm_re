import json
from urllib2 import Request, urlopen

from configurations.env_configs import RAILS_TOKEN

class APIService(object):
	def __init__(self):
		super(APIService, self).__init__()

	
	def request_filter(self, uri):
		print ("Sending request to:", uri)
		request = Request(uri)
		request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
		return json.loads(urlopen(request).read())