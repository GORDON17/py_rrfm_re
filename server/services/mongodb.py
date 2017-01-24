import os
from mongoengine import connect

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


from datetime import datetime
# from pymongo import MongoClient
from configurations.env_configs import *
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
	for index, row in df.iterrows():
		if id == row['account_id']:
			continue

		interest_count = row['interest_count']
		interest_similarity = row['interest_similarity']
		if type == INTEREST_TYPES['social']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__social_interest_count=interest_count,
																set__social_interest_similarity=interest_similarity) \
												.save()
		elif type == INTEREST_TYPES['business']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__business_interest_count=interest_count,
																set__business_interest_similarity=interest_similarity) \
												.save()
		elif type == INTEREST_TYPES['lifestyle']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__lifestyle_interest_count=interest_count,
																set__lifestyle_interest_similarity=interest_similarity) \
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
	jobs = Job.objects
	print jobs
	job_list = []
	for job in jobs:
		job_list.append(job.to_json())

	return job_list

from models.mutual_friend import MutualFriend

def update_mutual_friend_recommendations(commons):
	for key, value in commons.iteritems():
		MutualFriend.objects(account_id=value['parent'],
												 user_id=key) \
									.modify(upsert=True, 
													new=True, 
													set__connection_level=value['level'],
													set__num_of_mutual_friends=value['num_of_commons']) \
									.save()












