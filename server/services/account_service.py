import os, json, gc
import pandas as pd
from urllib2 import Request, urlopen

from configurations.env_configs import *

def _request_data(uri):
	print ("Sending request to:", uri)
	request=Request(uri)
	request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
	data = json.loads(urlopen(request).read())
	df = pd.DataFrame(data)
	print ("Data shape:", df.shape)
	return df

def get_accounts():
    df_accounts = _request_data(ACCOUNTS_URI)
    df_accounts['location'].fillna('empty', inplace=True)
    return df_accounts