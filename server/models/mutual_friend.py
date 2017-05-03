from mongoengine import *
from vault_templates import mutual_template
from configurations.constants import OBJECT_TYPES

class MutualFriend(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	connection_level = IntField(default=0)
	num_of_mutual_friends = IntField(default=0)
	created_at = DateTimeField(required=True)

	def to_vault_object(self):
		return {
			'id': self.user_id,
			'type': OBJECT_TYPES['USER']
		}

	def to_vault_target(self):
		return {
			'id': self.account_id,
			'type': OBJECT_TYPES['USER']
		}

	def to_mutual_vault_context(self):
		return {
			'text': mutual_template(self.user_id, self.num_of_mutual_friends),
			'status': "unread",
			'algorithm': "mutual_friend"
		}

	def to_mutual_vault_context_ops(self):
		return {
			'text': mutual_template(self.account_id, self.num_of_mutual_friends),
			'status': "unread",
			'algorithm': "mutual_friend_ops"
		}

	def to_vault_weight(self):
		return self.num_of_mutual_friends - (1.6 * self.connection_level)