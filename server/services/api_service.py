import json
from urllib import urlencode
from urllib2 import Request, urlopen

from configurations.env_configs import RAILS_TOKEN, API_LIMIT

class APIService(object):
	limit = API_LIMIT

	def __init__(self):
		super(APIService, self).__init__()

	
	def request_filter(self, uri):
		print ("Sending request to:", uri)
		request = Request(uri)
		request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
		return json.loads(urlopen(request).read())

	def get_request(self, uri):
		data = []
		offset = 0
		while True:
			params = urlencode({'limit':self.limit, 'offset':offset})
			url = uri + '?' + params
			print ("Sending request to:", url)
			request = Request(url)
			request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
			response = json.loads(urlopen(request).read())
			size = len(response)
			print ("Response size: ", size)
			if size < 1:
				break
			else:
				data += response
				offset += limit

			print("Total results: ", len(data))
			return data