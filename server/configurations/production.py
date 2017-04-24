import os

DEBUG = False
TESTING = False
MONGO_DBNAME = os.environ.get('DATABASE')
MONGO_URI = os.environ.get('MONGO_URL')
RAILS_TOKEN = os.environ.get('RAILS_TOKEN')