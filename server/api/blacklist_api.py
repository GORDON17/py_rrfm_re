from flask_restful import Api, Resource, reqparse
from flask import Blueprint, json, jsonify

from configurations.env_configs import *

blacklist_api = Api(Blueprint('blacklist_api', __name__))

@blacklist_api.resource("/blacklist")
class BlackApi(Resource):
	@staticmethod
	def post():
		
		