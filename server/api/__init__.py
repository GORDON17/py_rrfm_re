__all__ = ["mutual_friend", "similarity"]
from configurations.env_configs import *
import pdb

def check_token(parser):
	parser.add_argument('Token', type=str, required=True, location=['headers'], help='Token cannot be blank!')
	args = parser.parse_args()
	token = args['Token']

	if (token != RAILS_TOKEN):
		return False

	return True