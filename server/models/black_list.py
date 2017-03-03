from mongoengine import *

class BlackList(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	created_at = DateTimeField(required=True)