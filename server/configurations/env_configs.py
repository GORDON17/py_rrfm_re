import os

BASE_URI = os.environ.get('API_URI') or "http://0.0.0.0:3000/"
SOCIAL_INTERESTS_URI = BASE_URI + "api/v4/re/interests/social"
BUSINESS_INTERESTS_URI = BASE_URI + "api/v4/re/interests/business"
LIFESTYLE_INTERESTS_URI = BASE_URI + "api/v4/re/interests/lifestyle"
EVENT_TYPES_URI = BASE_URI + "api/v4/re/events/types"
CONNECTIONS_URI = BASE_URI + "api/v4/re/connections"
ACCOUNTS_URI = BASE_URI + "api/v4/re/accounts"

INTEREST_TYPES = {
	'social': 'social',
	'business': 'business',
	'lifestyle': 'lifestyle'
}
