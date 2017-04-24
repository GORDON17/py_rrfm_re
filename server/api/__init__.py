__all__ = ["mutual_friend", "similarity"]
from configurations.env_configs import *

def check_token(parser):
	parser.add_argument('token', type=str, help='Token cannot be blank!')
	args = parser.parse_args()
	token = args['token']
	if (token != RAILS_TOKEN):
		return False

	return True