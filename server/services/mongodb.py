import os
# from pymongo import MongoClient
from configurations.env_configs import *
from models.event_type_similarity import EventTypeSimilarity
from models.interest_similarity import InterestSimilarity

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

		if type == INTEREST_TYPES['social']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__social_interest_count=row['interest_count'],
																set__social_interest_similarity=row['interest_similarity']) \
												.save()
		elif type == INTEREST_TYPES['business']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__business_interest_count=row['interest_count'],
																set__business_interest_similarity=row['interest_similarity']) \
												.save()
		elif type == INTEREST_TYPES['lifestyle']:
			InterestSimilarity.objects(account_id=id,
																 user_id=row['account_id']) \
												.modify(upsert=True, 
																new=True, 
																set__lifestyle_interest_count=row['interest_count'],
																set__lifestyle_interest_similarity=row['interest_similarity']) \
												.save()

	print ("Updated:", InterestSimilarity.objects.count())







