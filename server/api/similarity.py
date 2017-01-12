from flask import Blueprint, json, jsonify
from flask_restful import Api, Resource, reqparse
from services.similarity_service import *
from services.mongodb import *

similarity_api = Api(Blueprint('similarity_api', __name__))

# @similarity_api.resource('/sim/e/<int:id>')
# class EventSimilarityAPI(Resource):
#     @staticmethod
#     def get(id):
#     	return events_sim(id).to_json(orient='records')

@similarity_api.resource('/sim/e/<int:id>')
class EventLocationSimilarityAPI(Resource):
    @staticmethod
    def get(id):
        parser = reqparse.RequestParser()
        parser.add_argument('location', type=str, help='Yada Yada Yada')
        args = parser.parse_args()
        location = args['location']

    	events_sim = events_sim_with_loc(id, location)
        update_events_table(id, events_sim)
        return events_sim.to_json(orient='records')

@similarity_api.resource('/sim/i/<int:id>')
class InterestSimilarityAPI(Resource):
    @staticmethod
    def get(id):
    	return interests_sim(id).to_json(orient='records')

@similarity_api.resource('/sim/i/<location>/<int:id>')
class InterestLocationSimilarityAPI(Resource):
    @staticmethod
    def get(id, location):
    	return interests_sim_with_loc(id, location).to_json(orient='records')
