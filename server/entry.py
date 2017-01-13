from app import app
import os
from mongoengine import connect

ENV = os.environ.get('SERVER_ENV')
if ENV != "production":
  from configurations.development import MONGO_URI, MONGO_DBNAME
  connect(
    db=MONGO_DBNAME,
    host=MONGO_URI
  )
  print "Mongodb(development) is runing on: "
  print MONGO_URI
else:
  from configurations.production import MONGO_URI, MONGO_DBNAME
  connect(
    db=MONGO_DBNAME,
    host=MONGO_URI
  )
  print "Mongodb(production) is runing on: "
  print MONGO_URI


if __name__ == '__main__':
    app.run()
