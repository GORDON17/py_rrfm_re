def interest_template(isPlain, user_id, sim_percent):
	percent = int(sim_percent * 100)

	if isPlain:
		text = "Talk to {{user-%d}} as you have %d%% interests in common!" \
					% (user_id, percent)
	else:
		markup = "Talk to <b>{{user-%d}}</b> as you have %d%% interests in common!" \
					% (user_id, percent)

	return text

def mutual_template(isPlain, user_id, num_of_mutual_friends):
	if isPlain:
		text = "Talk to {{user-%d}} as you have %d mutual friends!" % (user_id, num_of_mutual_friends)
	else:
		text = "Talk to <b>{{user-%d}}</b> as you have %d mutual friends!" % (user_id, num_of_mutual_friends)
	
	return text