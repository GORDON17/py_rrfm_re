from mongoengine import *
from vault_templates import interest_template
from configurations.constants import (OBJECT_TYPES, INTEREST_TYPES)

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

	def to_interest_vault_context(self):
		return {
			'text': interest_template(self.user_id, self.to_vault_weight()),
			'status': "unread",
			'algorithm': "social_interest_similarity"
		}

	def to_interest_vault_context_ops(self):
		return {
			'text': interest_template(self.account_id, self.to_vault_weight()),
			'status': "unread",
			'algorithm': "social_interest_similarity"
		}

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

	def to_vault_weight(self):
		count = 0
		if self.social_interest_similarity != 0:
			count += 1

		if self.business_interest_similarity != 0:
			count += 1

		if self.lifestyle_interest_similarity != 0:
			count += 1

		return (self.social_interest_similarity + self.business_interest_similarity + self.lifestyle_interest_similarity) / count


