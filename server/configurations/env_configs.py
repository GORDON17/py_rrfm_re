import os

RAILS_TOKEN = os.environ.get('RAILS_TOKEN') or 'c30a7641-0d2b-4fdc-9cd5-1c2d85905726'
BASE_URI = os.environ.get('API_URI') or "http://0.0.0.0:3000/"
SOCIAL_INTERESTS_URI = BASE_URI + "api/v4/re/interests/social"
BUSINESS_INTERESTS_URI = BASE_URI + "api/v4/re/interests/business"
LIFESTYLE_INTERESTS_URI = BASE_URI + "api/v4/re/interests/lifestyle"
EVENT_TYPES_URI = BASE_URI + "api/v4/re/events/types"
CONNECTIONS_URI = BASE_URI + "api/v4/re/connections"
ACCOUNTS_URI = BASE_URI + "api/v4/re/accounts"
MONTH_COUNT_URI = BASE_URI + "api/v4/re/month-count"
CONNECTIONS_FILTER = BASE_URI + "api/v4/re/filters/connections"
DECISIONS_FILTER = BASE_URI + "api/v4/re/filters/decisions"


VAULT_URI = os.environ.get('VAULT_URI') or "http://testvault.ivy.com"
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SERET_ACCESS_KEY = os.environ.get('AWS_SERET_ACCESS_KEY')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')

BATCH_SIZE = int(os.environ.get('BATCH_SIZE')) or 500
API_LIMIT = int(os.environ.get('API_LIMIT')) or 500