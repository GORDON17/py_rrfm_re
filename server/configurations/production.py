import os

DEBUG = False
TESTING = False
# MONGO_HOST = "mongodb://gordon:!QAZ@WSX!@@ds161048.mlab.com"
# MONGO_PORT = 61048
MONGO_DBNAME = "ivyre"
MONGO_URI = os.environ.get('MONGO_URL')#"mongodb://gordon:123123123@ds161048.mlab.com:61048/ivyre"