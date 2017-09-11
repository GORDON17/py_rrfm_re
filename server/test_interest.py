import os, json, gc, copy
import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.stats import pearsonr
from urllib2 import Request, urlopen
from pandas.io.json import json_normalize
from configurations.env_configs import *

from guppy import hpy
h = hpy()
h.setref()

# refactor for performance
# from mongodb import update_interests_table
from services.api_service import *

def _request_data(uri):
	print ("Sending request to:", uri)
	request = Request(uri)
	request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
	data = json.loads(urlopen(request).read())

	df = pd.DataFrame(data)
	print ("Requested data shape:", df.shape)
	return df


def _filtered_profile_matrix(df, profile, params, connections_data, decisions_data):
		df_copy = df.copy()
		if params['location'] and profile.location != 'empty':
				df_copy = df_copy[(df_copy.location.str.contains(profile.location))] #(df_copy.location == '') | (df_copy.location == 'empty') | 

		if params['chapter'] and profile.chapter != 0:
				df_copy = df_copy[(df_copy.chapter == profile.chapter)]

		if params['nationality'] and profile.nationality != 'empty':
				df_copy = df_copy[(df_copy.nationality == profile.nationality)]

		df_copy = df_copy[(df_copy.account_id != _isConnected(profile.account_id, df_copy.account_id, connections_data)) & (df_copy.account_id != _isDecided(profile.account_id, df_copy.account_id, decisions_data))]

		return df_copy


def _manipulate_profile_matrix(df):
		df_profile = copy.deepcopy(df)
		df_profile[['account_id']] = df_profile[['account_id']].astype(int)
		df_profile[['chapter']] = df_profile[['chapter']].astype(int)
		df_profile['location'].fillna('empty', inplace=True)
		df_profile['nationality'].fillna('empty', inplace=True)
		df_profile['chapter'].fillna(0, inplace=True)
		df_profile_t = pd.pivot_table(df_profile.copy(), index=['account_id', 'location', 'nationality', 'chapter'], columns=['social'], values='indicator')
		
		df_profile_t.reset_index(inplace=True)
		df_profile_t.fillna(value=0, inplace=True)
		df_profile_t.dropna(inplace=True)
		df_profile_t.sort_values(by='account_id', ascending=True, inplace=True)
		df_profile_t.reset_index(drop=True, inplace=True)

		del df_profile
		return df_profile_t


def _calculate_similarity(df, offset, size):
		return _calculate_matching_distance(df, offset, size)

def _convert_to_double(X):
		return np.ascontiguousarray(X, dtype=np.double)

def _calculate_matching_distance(X, offset, size):
		s = X.shape
		if len(s) != 2:
				raise ValueError('A 2-dimensional array must be passed.')
		
		X = np.asarray(X, order='c')
		m, n = s
		X = _convert_to_double(X)
		
		results = []
		k = offset
		c = 0
		end = m if offset + size > m else offset + size

		for i in xrange(offset, end):
				dm = np.zeros(m, dtype=np.double)

				for j in xrange(0, m):
						if X[i].shape != X[j].shape:
								raise ValueError('The 1d arrays must have equal lengths.')

						dm[j] = (X[i] != X[j]).mean()
						k = k + 1

				results.append(dm)
				c = c + 1

		return results

def _request_connections_filter(uri):
		print ("Sending request to:", uri)
		request = Request(uri)
		request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
		return json.loads(urlopen(request).read())

def _isConnected(account_id, user_id, connections_data):
		if connections_data.get(str(account_id)) is None or connections_data[str(account_id)]['connections'].get(str(user_id)) is None:
				return 0
		
		return user_id if connections_data[str(account_id)]['connections'][str(user_id)] == 1 else 0

def _isDecided(account_id, user_id, decisions_data):
	if decisions_data.get(str(account_id)) is None or decisions_data[str(account_id)]['decisions'].get(str(user_id)) is None:
		return 0

	return user_id if decisions_data[str(account_id)]['decisions'][str(user_id)] == 1 or decisions_data[str(account_id)]['decisions'][str(user_id)] == 2 else 0

def process_interest_similarity(uri, type, params):
				structured_df = _manipulate_profile_matrix(_request_data(uri))
				print ("Structured profile matrix shape:", structured_df[structured_df.columns[4:]].shape)
				connections_data = APIService().get_request(CONNECTIONS_FILTER, '', 1000, 'dict')
				decisions_data = APIService().get_request(DECISIONS_FILTER, "trackable_type=Account", 1000, 'dict')
				row_count, column_count = structured_df[structured_df.columns[4:]].shape

				offset = 0

				prepared_df = structured_df[['account_id', 'location', 'nationality', 'chapter']].copy()
				for i in xrange(0, row_count, BATCH_SIZE):
						print 'Processing records: ', i, ' to ', i + BATCH_SIZE
						list_interest_sim = _calculate_similarity(structured_df[structured_df.columns[4:]].copy(), i, BATCH_SIZE)

						count = 0
						for index, profile in prepared_df[i:(i+BATCH_SIZE)].iterrows():
								sim_list = pd.Series(list_interest_sim[count].tolist())
								df = copy.deepcopy(prepared_df)
								df['interest_similarity'] = 1 - sim_list.values
								df['interest_count'] = (1 - sim_list.values) * column_count
								df['interest_count'] = df['interest_count'].astype(int)

								df_profile_r = _filtered_profile_matrix(df, profile, params, connections_data, decisions_data).sort_values(by='interest_similarity', ascending=0)[1:10]
								print df_profile_r
								del df
								# update_interests_table(profile.account_id, df_profile_r, type)
								print('Processed interest similarity for account: ', profile.account_id)
								count += 1

						del list_interest_sim


if __name__ == '__main__':
	uri = 'http://0.0.0.0:3000/api/v4/re/interests/social'
	params = {
		'location': True,
		'chapter': True,
		'nationality': True
	}
	process_interest_similarity(uri, '', params)


