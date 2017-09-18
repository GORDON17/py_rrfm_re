import json
from urllib import urlencode
from urllib2 import Request, urlopen
import collections

from configurations.env_configs import RAILS_TOKEN, API_LIMIT

class APIService(object):
	g_limit = API_LIMIT

	def __init__(self):
		super(APIService, self).__init__()

	
	def request_filter(self, uri):
		print ("Sending request to:", uri)
		request = Request(uri)
		request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
		return json.loads(urlopen(request).read())

	def get_request(self, uri, params="", l_limit=None, response_type='list'):
		data = {
        'list': [],
        'dict': {},
    }[response_type]

		offset = 0
		limit = l_limit if l_limit is not None else self.g_limit

		while True:
			limitation = urlencode({'limit':limit, 'offset':offset})
			url = uri + '?' + params + '&' + limitation
			print ("Sending request to:", url)
			request = Request(url)
			request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
			response = json.loads(urlopen(request).read())
			size = len(response)
			print ("Response size: ", size)
			if size < 1:
				break
			else:
				if response_type == 'list':
					data += response
				elif response_type == 'dict':
					self.__update(data, response)
					
				offset += limit

		print("Total results: ", len(data))
		return data

	def __update(self, d, u):
    for k, v in u.iteritems():
        if isinstance(d, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = self.__update(d.get(k, {}), v)
                d[k] = r
            else:
                d[k] = u[k]
        else:
            d = {k: u[k]}
    return d