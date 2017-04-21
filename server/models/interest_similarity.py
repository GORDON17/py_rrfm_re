from mongoengine import *
from vault_templates import *

class InterestSimilarity(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	social_interest_similarity = FloatField(default=0)
	social_interest_count = IntField(default=0)
	business_interest_similarity = FloatField(default=0)
	business_interest_count = IntField(default=0)
	lifestyle_interest_similarity = FloatField(default=0)
	lifestyle_interest_count = IntField(default=0)
	created_at = DateTimeField(required=True)

	def to_social_interest_vault_context(self):
		return {
			'text': social_interest_template(self),
			'status': "unread",
			'algorithm': "social_interest_similarity"
		}

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