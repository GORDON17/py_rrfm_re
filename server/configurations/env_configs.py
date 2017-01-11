import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    MONGO_DBNAME = "ivyre"

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    # MONGO_HOST = "mongodb://gordon:!QAZ@WSX!@@ds161048.mlab.com"
    # MONGO_PORT = 61048
    MONGO_DBNAME = "ivyre"
    MONGO_URI = os.environ.get('MONGODB_URI') or os.environ.get('MONGO_URL')

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    # MONGO_HOST = "mongodb://GaoYuantekiMacBook-Pro.local"
    # MONGO_PORT = 27017
    MONGO_DBNAME = "ivyre"
    MONGO_URI = "mongodb://GaoYuantekiMacBook-Pro.local:27017/ivyre"