import os, pdb
from mongoengine.connection import (connect, disconnect)

def connect_db():
  ENV = os.environ.get('SERVER_ENV')
  print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%A"))
  if ENV != "production":
    from configurations.development import MONGO_URI, MONGO_DBNAME
    connect(
      db=MONGO_DBNAME,
      host=MONGO_URI
    )
    print "Mongodb(development) is runing on: "
    print MONGO_URI
  else:
    from configurations.production import MONGO_URI, MONGO_DBNAME
    connect(
      db=MONGO_DBNAME,
      host=MONGO_URI
    )
    print "Mongodb(production) is runing on: "
    print MONGO_URI

def disconnect_db():
	disconnect()

from datetime import datetime
# from pymongo import MongoClient
from configurations.env_configs import *
from configurations.constants import *
from models.event_type_similarity import EventTypeSimilarity
from models.interest_similarity import InterestSimilarity
from models.job import Job

# def create_db():
# 	ENV = os.environ.get('SERVER_ENV')
# 	if ENV != "production":
# 		from configurations.development import MONGO_URI, MONGO_DBNAME
# 		client = MongoClient(MONGO_URI)
# 		print "Mongodb(development) is runing on: "
# 		print MONGO_URI
# 	else:
# 		from configurations.production import MONGO_URI, MONGO_DBNAME
# 		client = MongoClient(MONGO_URI)
# 		print "Mongodb(production) is runing on: "
# 		print MONGO_URI

# 	return client[MONGO_DBNAME]



# def update_events_table(id, df):
	# db = create_db()
	# # db.events_similarity_table.remove({}) 

	# for index, row in df.iterrows():
	# 	db.events_similarity_table.update_one(
	# 		{
	# 			"account_id": id,
	# 			"user_id": row['account_id']
	# 		},
	# 		{
	# 			"$set": {
	# 				"similarity_percentage": row['similarity_percentage'] 
	# 			}
	# 		},
	# 		upsert=True
	# 	)

	# print db.events_similarity_table.count()

def update_events_table(id, df):
	for index, row in df.iterrows():
		EventTypeSimilarity.objects(account_id=id, user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__similarity_percentage=row['similarity_percentage']) \
												.save()

	print ("Updated:", EventTypeSimilarity.objects.count())

def update_interests_table(id, df, type):
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	for index, row in df.iterrows():
		if id == row['account_id']:
			continue

		interest_count = row['interest_count']
		interest_similarity = row['interest_similarity']
		
		if type == INTEREST_TYPES['SOCIAL']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__social_interest_count=interest_count,
																set__social_interest_similarity=interest_similarity,
																set__created_at=time_now) \
												.save()
		elif type == INTEREST_TYPES['BUSINESS']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__business_interest_count=interest_count,
																set__business_interest_similarity=interest_similarity,
																set__created_at=time_now) \
												.save()
		elif type == INTEREST_TYPES['LIFESTYLE']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__lifestyle_interest_count=interest_count,
																set__lifestyle_interest_similarity=interest_similarity,
																set__created_at=time_now) \
												.save()

	# print ("Updated:", InterestSimilarity.objects.count())


def add_job(job_id, name):
	print('starting saving job')
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	new_job = Job(job_id=job_id, name=name, state=0, duration=0, created_at=time_now)
	new_job.save() 

	# new_job = Job.objects(job_id=job_id,
	# 											 name=name) \
	# 							.modify(upsert=True, 
	# 											new=True, 
	# 											set__state=0,
	# 											set__duration=0,
	# 											set__created_at=datetime.now()) \
	# 							.save()
	if new_job.id == new_job.pk:
		print('Job: ' + str(new_job.name) + ', state: ' + str(new_job.state))
		return new_job.id
	else:
		print("Couldn't create the job.")
		return None

def update_job_state(job_obj_id, state):
	print "updating job"
	job = Job.objects.with_id(job_obj_id)
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	dt = datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S") - job.created_at
	duration = dt.seconds

	try:
		job.state = state
		job.duration = duration
		job.ended_at = time_now
		job.save()
		print('Job: ' + str(job.name) + ', state: ' + str(job.state) + ', duration: ' + str(job.duration))
	except:
		print('ERROR!')


def get_jobs():
	connect_db()
	print 'receiving jobs ...'
	jobs = Job.objects

	job_list = []
	for job in jobs:
		job_list.append(job.to_json())

	disconnect_db()
	return job_list

from models.mutual_friend import MutualFriend

def update_mutual_friend_recommendations(commons):
	time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	for key, value in commons.iteritems():
		MutualFriend.objects(account_id=value['parent'],
												 user_id=key) \
									.modify(upsert=True, 
													new=True, 
													set__connection_level=value['level'],
													set__num_of_mutual_friends=value['num_of_commons'],
													set__created_at=time_now) \
									.save()


def build_interest_recommendation_vault_objects():
	vaults = []

	objects = InterestSimilarity.objects
	for obj in objects:
		if obj.social_interest_similarity and obj.social_interest_count:
			vault = _build_vault_object(obj.to_vault_object(), obj.to_vault_target(), obj.to_social_interest_vault_context())
			vaults.append(vault)

	return vaults


def _build_vault_object(obj, target, context):
	return	{
						'actor': {
							'type': "Service",
			        'name': "IVY Recommendation"
			    	},
			    	'object': obj,
			    	'target': target,
			    	'context': context
					}







