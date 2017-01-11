import os
from logging import StreamHandler
from sys import stdout
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

def create_app():
    from api.similarity import similarity_api
    from api.mutual_friend import mutual_friend_api
    from views.index import index_view

    app = Flask(__name__)

    ENV = os.environ.get('SERVER_ENV')
    if ENV != "production":
        app.config.from_object('configurations.development')
    else:
        app.config.from_object('configurations.production')

    app.register_blueprint(similarity_api.blueprint, url_prefix='/api')
    app.register_blueprint(mutual_friend_api.blueprint, url_prefix='/api')
    app.register_blueprint(index_view)

    # db.init_app(app)

    handler = StreamHandler(stdout)
    app.logger.addHandler(handler)
    return app


app = create_app()

client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DBNAME']]

# db = PyMongo(app).db





