from mongoengine import *

class BlackList(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	created_at = DateTimeField(required=True)

	@staticmethod
	def is_blacklist(account_id, user_id):
		return BlackList.objects(account_id=account_id, user_id=user_id).count() > 0