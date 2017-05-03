def interest_template(user_id, sim_percent):
	percent = int(sim_percent * 100)
	text = "Talk to <b>%d</b> as you have %d%% interests in common!" \
					% (user_id, percent)
	return text

def mutual_template(user_id, num_of_mutual_friends):
	text = "Talk to <b>%d</b> as you have %d mutual friends!" % (user_id, num_of_mutual_friends)
	return text