import os
from pymongo import MongoClient

def create_db():
	ENV = os.environ.get('SERVER_ENV')
	if ENV != "production":
		from configurations.development import MONGO_URI, MONGO_DBNAME
		client = MongoClient(MONGO_URI)
	else:
		from configurations.production import MONGO_URI, MONGO_DBNAME
		client = MongoClient(MONGO_URI)

	return client[MONGO_DBNAME]