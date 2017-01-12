import os

BASE_URI = os.environ.get('API_URI') or "http://0.0.0.0:3000/"
SOCIAL_INTERESTS_URI = BASE_URI + "api/v4/re/interests/social"
EVENT_TYPES_URI = BASE_URI + "api/v4/re/events/types"