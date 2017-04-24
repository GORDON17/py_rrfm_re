def social_interest_template(interest_similarity_object):
	obj = interest_similarity_object
	sim_percent = int(obj.social_interest_similarity * 100)
	text = "Talk to [%d] as you have %d%% (%d) social interests in common!" \
					% (obj.user_id, sim_percent, obj.social_interest_count)
	return text

def mutual_template(mutual_friend_object):
	obj = mutual_friend_object
	text = "Talk to [%d] as you have %d mutual friends!" % (obj.user_id, obj.num_of_mutual_friends)
	return text