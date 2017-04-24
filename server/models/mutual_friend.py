from mongoengine import *
from vault_templates import mutual_template

class MutualFriend(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	connection_level = IntField(default=0)
	num_of_mutual_friends = IntField(default=0)
	created_at = DateTimeField(required=True)

	def to_vault_object(self):
		return {
			'id': self.user_id,
			'type': "user"
		}

	def to_vault_target(self):
		return {
			'id': self.account_id,
			'type': "user"
		}

	def to_mutual_vault_context(self):
		return {
			'text': mutual_template(self),
			'status': "unread",
			'algorithm': "mutual_friend"
		}