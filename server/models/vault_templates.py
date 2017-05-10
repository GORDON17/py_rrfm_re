def interest_template(isPlain, user_id, sim_percent):
	percent = int(sim_percent * 100)

	if isPlain:
		text = "Meet {{user-%d}} as you have %d%% interests in common" \
					% (user_id, percent)
	else:
		text = "Meet <b>{{user-%d}}</b> as you have %d%% interests in common" \
					% (user_id, percent)

	return text

def mutual_template(isPlain, user_id, num_of_mutual_friends):
	if isPlain:
		text = "Meet {{user-%d}} as you have %d mutual friends in common" % (user_id, num_of_mutual_friends)
	else:
		text = "Meet <b>{{user-%d}}</b> as you have %d mutual friends in common" % (user_id, num_of_mutual_friends)
	
	return text