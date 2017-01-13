from mongoengine import *

class InterestSimilarity(DynamicDocument):
	account_id = IntField(required=True)
	user_id = IntField(required=True)
	social_interest_similarity = FloatField(default=0)
	social_interest_count = IntField(default=0)
	business_interest_similarity = FloatField(default=0)
	business_interest_count = IntField(default=0)
	lifestyle_interest_similarity = FloatField(default=0)
	lifestyle_interest_count = IntField(default=0)