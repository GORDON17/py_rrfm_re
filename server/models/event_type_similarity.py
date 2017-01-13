from mongoengine import *

class EventTypeSimilarity(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	similarity_percentage = FloatField(default=0)