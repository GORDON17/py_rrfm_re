import os

DEBUG = False
TESTING = False
# MONGO_HOST = "mongodb://gordon:!QAZ@WSX!@@ds161048.mlab.com"
# MONGO_PORT = 61048
MONGO_DBNAME = "ivyre"
MONGO_URI = os.environ.get('MONGODB_URI') or os.environ.get('MONGO_URL')