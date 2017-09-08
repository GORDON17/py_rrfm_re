import json
from urllib2 import Request, urlopen

from configurations.env_configs import RAILS_TOKEN

class APIService(object):
  limit = 1000

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
        params = urlencode({'limit':self.limit, 'offset':self.offset})
        url = uri + '?' + params
        print ("Sending request to:", url)
        request = Request(url)
        request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
        data += json.loads(urlopen(request).read())

        if len(data) == 0:
            break
        else:
            offset += limit

        return data