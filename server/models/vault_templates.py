def social_interest_template(interest_similarity_object):
	obj = interest_similarity_object
	text = "Talk to [%d] as you have %d% (%d) social interests in common!" \
					% (obj.account_id, int(obj.social_interest_similarity)*100, obj.social_interest_count)
	return text