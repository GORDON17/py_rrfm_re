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

def _request_data(uri):
	print ("Sending request to:", uri)
	request = Request(uri)
	request.add_header('HTTP_X_IVY_SESSION_TOKEN', RAILS_TOKEN)
	data = json.loads(urlopen(request).read())

	df = pd.DataFrame(data)
	print ("Requested data shape:", df.shape)
	return df


def _convert_to_double(X):
    return np.ascontiguousarray(X, dtype=np.double)

# def _calculate_matching_distance(X, offset, size):
# 		s = X.shape
# 		if len(s) != 2:
# 				raise ValueError('A 2-dimensional array must be passed.')
		
# 		X = np.asarray(X, order='c')
		
# 		m, n = s
# 		dm = np.zeros((m * (m - 1)) // 2, dtype=np.double)

# 		X = _convert_to_double(X)
		
# 		k = offset
# 		for i in xrange(offset, offset + size):
# 			print 'i: ', i
# 				for j in xrange(0, m):
# 						print 'k: ', k
# 						print 'j: ', j
# 						if X[i].shape != X[j].shape:
# 								raise ValueError('The 1d arrays must have equal lengths.')
# 						dm[k] = (X[i] != X[j]).mean()
# 						k = k + 1

# 		pdb.set_trace()
# 		return dm


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
		profile_D = distance.squareform(distance.pdist(df, metric='matching'))
		pdb.set_trace()
		
		return profile_D #_calculate_matching_distance(df, offset, size)


def process_interest_similarity(uri, type, params):
		structured_df = _manipulate_profile_matrix(_request_data(uri))

		# df_profile_t = structured_df[structured_df.columns[4:]]
		print ("Structured profile matrix shape:", structured_df[structured_df.columns[4:]].shape)
		row_count, column_count = structured_df[structured_df.columns[4:]].shape

		offset = 0
		size = 3

		for i in xrange(0, row_count, size):
			df_interest_sim = _calculate_similarity(structured_df[structured_df.columns[4:]], i, size)
			# del df_profile_t
			# gc.collect()

			count = 1
			prepared_df = structured_df[['account_id', 'location', 'nationality', 'chapter']].copy()

			for index, profile in prepared_df[i:(i+size)].iterrows():
					print index
					sim_for_account = df_interest_sim[index].tolist()
					sim_list = pd.Series(sim_for_account)
					df = prepared_df.copy()
					df['interest_similarity'] = 1 - sim_list.values
					df['interest_count'] = (1 - sim_list.values) * column_count
					df['interest_count'] = df['interest_count'].astype(int)

					df_profile_f = _filtered_profile_matrix(df, profile, params) #df[(df.location == '') | (df.location == 'empty') | (df.location.str.contains(profile.location))]
					df_profile_r = df_profile_f.sort_values(by='interest_similarity', ascending=0)[1:10]
					# update_interests_table(profile.account_id, df_profile_r, type)
					print('Processed interest similarity for account: ', profile.account_id)
					count += 1

		del df_interest_sim
		del prepared_df
		gc.collect()





if __name__ == '__main__':
	uri = 'http://0.0.0.0:3000/api/v4/re/interests/social'
	params = {
		'location': True,
		'chapter': True,
		'nationality': True
	}
	process_interest_similarity(uri, '', params)


