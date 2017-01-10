import os
import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.stats import pearsonr

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
	df_new = _matrix_with_loc(location)

	df_profile_t = df_new[df_new.columns[14:]]
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
	df_new = _matrix_with_loc(location)

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

def _matrix_with_loc(location):
	df_profile = pd.read_csv(_datasets_path() + 'profile_dataset.csv', names=['V1', 'V2', 'V3', 'V4'])
	df_profile['V4'].fillna('empty', inplace=True)
	# df_profile = df_profile.pivot(index='V1', columns='V2', values='V3')
	df_profile = pd.pivot_table(df_profile, index=['V1', 'V4'], columns='V2', values='V3')
	df_profile_t = df_profile.reset_index()
	df_profile_t = df_profile_t.fillna(value=0)
	df_profile_t = df_profile_t[(df_profile_t.V4 == 'empty') | (df_profile_t.V4.str.contains(location))]
	print(df_profile_t.shape)
	# print df_profile_t[df_profile_t.V1 == 28071]

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

def _index_of(id, matrix):
	print id
	return matrix[matrix.V1 == id].index.tolist()[0]

def _datasets_path():
	return os.path.abspath("") + "/datasets/"
