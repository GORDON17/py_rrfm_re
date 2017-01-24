import sys, os
from flask import Blueprint, json, jsonify
from flask_restful import Api, Resource

from services.bfs_service import *
from configurations.env_configs import *

mutual_friend_api = Api(Blueprint('mutual_friend_api', __name__))

@mutual_friend_api.resource("/mutual/<int:id>")
class BFSAPI(Resource):
    @staticmethod
    def get(id):
			g = graph(CONNECTIONS_URI)
			results = bfs(g, id)
			return json.dumps(results)

@mutual_friend_api.resource("/mutualtesting")
class BFSAPITest(Resource):
    @staticmethod
    def get():
			process_mutual_friends(CONNECTIONS_URI)
			return "mutual friend testing done."

			

@mutual_friend_api.resource("/collections")
class DBCollections(Resource):
    @staticmethod
    def get():
			return json.dumps(create_db().collection_names())

