import os, json, gc
import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.stats import pearsonr
from urllib2 import Request, urlopen
from pandas.io.json import json_normalize
from configurations.env_configs import SOCIAL_INTERESTS_URI, EVENT_TYPES_URI

def interests_sim(id):
	df_new = _matrix()

	df_profile_t = df_new[df_new.columns[13:]]
	print df_profile_t.shape

	index = _index_of(id, df_new)

	profile_d = distance.pdist(df_profile_t, metric='matching')
	profile_D = distance.squareform(profile_d)

	p_r = profile_D[index].tolist()
	sim = pd.Series(p_r)
	df_new['count_of_interests'] = (1 - sim.values) * len(df_profile_t.columns)
	df_new['count_of_interests'] = df_new['count_of_interests'].astype(int)
	List = [i[0] for i in sorted(enumerate(p_r), key=lambda x:x[1])][0:21]
	
	return df_new.ix[List][['V2', 'count_of_interests']]#['V2']


def interests_sim_with_loc(id, location):
	# df_new = _matrix_with_loc(location)
	# df_profile_t = df_new[df_new.columns[14:]]
	df_new = _interests_matrix_with_loc(location)
	df_profile_t = df_new[df_new.columns[2:]]

	index = _index_of(id, df_new)

	profile_d = distance.pdist(df_profile_t, metric='matching')
	profile_D = distance.squareform(profile_d)
	p_r = profile_D[index].tolist()
	del profile_d
	del profile_D
	gc.collect()

	sim = pd.Series(p_r)
	df_new['count_of_interests'] = (1 - sim.values) * len(df_profile_t.columns)
	df_new['count_of_interests'] = df_new['count_of_interests'].astype(int)
	List = [i[0] for i in sorted(enumerate(p_r), key=lambda x:x[1])][0:21]

	return df_new.ix[List][['account_id', 'count_of_interests']]#['V2']


def events_sim(id):
	df_new = _matrix()

	df_event_t = df_new[df_new.columns[2:13]]
	index = _index_of(id, df_new)

	df_event_t = df_event_t.div(df_event_t.sum(axis=1), axis=0)

	# event_D = np.corrcoef(df_event_t)
	# e_r = event_D[index].tolist()
	# sim = pd.Series(e_r)
	# df_new['similarity_percentage'] = sim.values
	# List = [i[0] for i in sorted(enumerate(e_r), key=lambda x:x[1], reverse=True)][0:21]
	# print event_D.shape

	event_d = distance.pdist(df_event_t, metric='euclidean')
	event_D = distance.squareform(event_d)
	e_r = event_D[index].tolist()
	sim = pd.Series(e_r)
	df_new['similarity_percentage'] = 1 - sim.values
	List = [i[0] for i in sorted(enumerate(e_r), key=lambda x:x[1])][0:21]

	return df_new.ix[List][['V2', 'similarity_percentage']]#['V2']


def events_sim_with_loc(id, location):
	df_new = _events_matrix_with_loc(location)
	df_event_t = df_new[df_new.columns[2:]]

	index = _index_of(id, df_new)

	df_event_t = df_event_t.div(df_event_t.sum(axis=1), axis=0)

	# event_D = np.corrcoef(df_event_t)
	# e_r = event_D[index].tolist()
	# sim = pd.Series(e_r)
	# df_new['similarity_percentage'] = sim.values
	# List = [i[0] for i in sorted(enumerate(e_r), key=lambda x:x[1], reverse=True)][0:21]
	# print event_D.shape

	event_d = distance.pdist(df_event_t, metric='correlation')
	event_D = distance.squareform(event_d)
	del df_event_t
	del event_d

	e_r = event_D[index].tolist()
	del event_D

	gc.collect()

	sim = pd.Series(e_r)
	df_new['similarity_percentage'] = 1 - sim.values
	
	# List = [i[0] for i in sorted(enumerate(e_r), key=lambda x:x[1])][0:21]
	# return df_new.ix[List][['account_id', 'email', 'similarity_percentage']]#['V2']
	return df_new

def _matrix_with_loc(location):
	df_profile = _social_interests_data()
	df_profile[['account_id']] = df_profile[['account_id']].astype(int)
	df_profile['location'].fillna('empty', inplace=True)
	df_profile = pd.pivot_table(df_profile, index=['account_id', 'location'], columns='social', values='indicator')
	df_profile_t = df_profile.reset_index()
	df_profile_t = df_profile_t.fillna(value=0)
	df_profile_t = df_profile_t[(df_profile_t.location == '') | (df_profile_t.location == 'empty') | (df_profile_t.location.str.contains(location))]

	df_event = _event_types_data()
	df_event[['account_id']] = df_event[['account_id']].astype(int)
	df_event[['count']] = df_event[['count']].astype(int)
	df_event[['event_type']] = df_event[['event_type']].astype(int)
	df_event = pd.pivot_table(df_event, index=['account_id', 'email'], columns='event_type', values='count')
	df_event_t = df_event.reset_index()
	df_event_t = df_event_t.fillna(value=0)

	df_new = df_event_t.set_index('account_id').join(df_profile_t.set_index('account_id'))
	df_new = df_new.dropna()
	df_new = df_new.sort_values(by='email', ascending=False)
	df_new = df_new.reset_index()
	print df_new[df_new.account_id == 28071].index.tolist()[0]
	return df_new


def _matrix():
	df_profile = pd.read_csv(_datasets_path() + 'profile dataset.csv', names=['V1', 'V2', 'V3'])
	df_profile = df_profile.pivot(index='V1', columns='V2', values='V3')
	df_profile_t = df_profile.reset_index()
	df_profile_t = df_profile_t.fillna(value=0)
	print(df_profile_t.shape)

	df_event = pd.read_csv(_datasets_path() + 'query event type.csv', names=['V1', 'V2', 'V3', 'V4'])
	df_event = pd.pivot_table(df_event, index=['V1', 'V2'], columns='V3', values='V4')
	df_event_t = df_event.reset_index()
	df_event_t = df_event_t.fillna(value=0)
	print(df_event_t.shape)

	df_new = df_event_t.set_index('V1').join(df_profile_t.set_index('V1'))
	print df_new.shape
	df_new = df_new.dropna()
	df_new = df_new.sort_values(by='V2', ascending=False)
	df_new = df_new.reset_index()
	print df_new.shape

	return df_new


def _index_of(id, df):
	print id
	return df[df.account_id == id].index.tolist()[0]


def _datasets_path():
	return os.path.abspath("") + "/datasets/"


def _social_interests_data():
    request=Request(SOCIAL_INTERESTS_URI)
    profiles = json.loads(urlopen(request).read())
    df = pd.DataFrame(profiles)
    print df.shape
    return df


def _event_types_data():
    request=Request(EVENT_TYPES_URI)
    events = json.loads(urlopen(request).read())
    df = pd.DataFrame(events)
    print df.shape
    return df


def _interests_matrix_with_loc(location):
	df_profile = _social_interests_data()
	df_profile[['account_id']] = df_profile[['account_id']].astype(int)
	df_profile['location'].fillna('empty', inplace=True)
	df_profile_t = pd.pivot_table(df_profile, index=['account_id', 'location'], columns=['social'], values='indicator')
	del df_profile
	gc.collect()

	df_profile_t = df_profile_t.reset_index()
	df_profile_t = df_profile_t.fillna(value=0)
	df_profile_t = df_profile_t[(df_profile_t.location == '') | (df_profile_t.location == 'empty') | (df_profile_t.location.str.contains(location))]
	df_profile_f = df_profile_t.dropna()
	del df_profile_t
	gc.collect()

	df_profile_s = df_profile_f.sort_values(by='account_id', ascending=True)
	del df_profile_f
	gc.collect()

	df_profile_s.reset_index(drop=True, inplace=True)
	return df_profile_s


def _events_matrix_with_loc(location):
	df_event = _event_types_data()
	df_event[['account_id']] = df_event[['account_id']].astype(int)
	df_event[['count']] = df_event[['count']].astype(int)
	df_event[['event_type']] = df_event[['event_type']].astype(int)

	df_event_t = pd.pivot_table(df_event, index=['account_id', 'email'], columns='event_type', values='count')
	del df_event
	gc.collect()

	df_event_t.reset_index(inplace=True)
	df_event_t = df_event_t.fillna(value=0)
	df_event_s = df_event_t.sort_values(by='account_id', ascending=True)
	del df_event_t
	gc.collect()

	df_event_s.reset_index(drop=True, inplace=True)
	return df_event_s

