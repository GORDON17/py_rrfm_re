import os, json, gc, pdb
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
#         pdb.set_trace()
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
				
def _request_data(uri):
		print ("Sending request to:", uri)
		request = Request(uri)
		request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
		data = json.loads(urlopen(request).read())

		df = pd.DataFrame(data)
		print ("Requested data shape:", df.shape)
		return df


def _filtered_profile_matrix(df, profile, params):
		df_copy = df.copy()
		if params['location']:
				df_copy = df_copy[(df_copy.location.str.contains(profile.location))] #(df_copy.location == '') | (df_copy.location == 'empty') | 

		if params['chapter']:
				df_copy = df_copy[(df_copy.chapter == profile.chapter)]

		if params['nationality']:
				df_copy = df_copy[(df_copy.nationality == profile.nationality)]

		return df_copy


def _manipulate_profile_matrix(df):
				df_profile = df.copy()
				df_profile[['account_id']] = df_profile[['account_id']].astype(int)
				df_profile[['chapter']] = df_profile[['chapter']].astype(int)
				df_profile['location'].fillna('empty', inplace=True)
				df_profile['nationality'].fillna('empty', inplace=True)
				df_profile['chapter'].fillna(0, inplace=True)
				df_profile_t = pd.pivot_table(df_profile.copy(), index=['account_id', 'location', 'nationality', 'chapter'], columns=['social'], values='indicator')
				del df_profile
				gc.collect()
				
				df_profile_t.reset_index(inplace=True)
				df_profile_t.fillna(value=0, inplace=True)
				df_profile_t.dropna(inplace=True)
				
				df_profile_t.sort_values(by='account_id', ascending=True, inplace=True)
				
				df_profile_t.reset_index(drop=True, inplace=True)
				return df_profile_t


def _calculate_similarity(df, offset, size):
				# pdb.set_trace()
				# profile_D = distance.squareform()
				# pdb.set_trace()
				
				return _calculate_matching_distance(df, offset, size)#profile_D

import copy

def process_interest_similarity(uri, type, params):
				structured_df = _manipulate_profile_matrix(_request_data(uri))
				pdb.set_trace()
				# df_profile_t = structured_df[structured_df.columns[4:]]
				print ("Structured profile matrix shape:", structured_df[structured_df.columns[4:]].shape)
				row_count, column_count = structured_df[structured_df.columns[4:]].shape

				offset = 0

				prepared_df = structured_df[['account_id', 'location', 'nationality', 'chapter']].copy()
				for i in xrange(0, row_count, BATCH_SIZE):
						print 'process ', i
						list_interest_sim = _calculate_similarity(structured_df[structured_df.columns[4:]].copy(), i, BATCH_SIZE)
						# del df_profile_t
						# gc.collect()

						count = 0
            # pdb.set_trace()
						for index, profile in prepared_df[i:(i+BATCH_SIZE)].iterrows():
								print '---------------', index, profile.account_id
								sim_list = pd.Series(list_interest_sim[count].tolist())
								df = copy.deepcopy(prepared_df)
								df['interest_similarity'] = 1 - sim_list.values
								df['interest_count'] = (1 - sim_list.values) * column_count
								df['interest_count'] = df['interest_count'].astype(int)

								# df_profile_f = _filtered_profile_matrix(df, profile, params) #df[(df.location == '') | (df.location == 'empty') | (df.location.str.contains(profile.location))]
								df_profile_r = _filtered_profile_matrix(df, profile, params).sort_values(by='interest_similarity', ascending=0)[1:10]
								del df
								# update_interests_table(profile.account_id, df_profile_r, type)
								print profile.account_id
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


