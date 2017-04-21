from mongoengine import *

class MutualFriend(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	connection_level = IntField(default=0)
	num_of_mutual_friends = IntField(default=0)
	created_at = DateTimeField(required=True)