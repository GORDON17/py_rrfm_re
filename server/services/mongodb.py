import os
from pymongo import MongoClient

def create_db():
	ENV = os.environ.get('SERVER_ENV')
	if ENV != "production":
		from configurations.development import MONGO_URI, MONGO_DBNAME
		client = MongoClient(MONGO_URI)
		print "Mongodb(development) is runing on: "
		print MONGO_URI
	else:
		from configurations.production import MONGO_URI, MONGO_DBNAME
		client = MongoClient(MONGO_URI)
		print "Mongodb(production) is runing on: "
		print MONGO_URI

	return client[MONGO_DBNAME]



def update_events_table(id, df):
	db = create_db()
	# db.events_similarity_table.remove({}) 

	for index, row in df.iterrows():
		db.events_similarity_table.update_one(
			{
				"account_id": id,
				"user_id": row['account_id']
			},
			{
				"$set": {
					"similarity_percentage": row['similarity_percentage'] 
				}
			},
			upsert=True
		)

	print db.events_similarity_table.count()