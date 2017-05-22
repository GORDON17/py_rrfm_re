from flask import Blueprint, json, jsonify
from flask_restful import Api, Resource, reqparse
from services.similarity_service import *
from services.mongodb import *
from configurations.env_configs import *
from configurations.constants import *

similarity_api = Api(Blueprint('similarity_api', __name__))

# @similarity_api.resource('/sim/e/<int:id>')
# class EventSimilarityAPI(Resource):
#     @staticmethod
#     def get(id):
#     	return events_sim(id).to_json(orient='records')

# @similarity_api.resource('/similarity/events')
# class EventLocationSimilarityAPI(Resource):
#     @staticmethod
#     def get():
#         parser = reqparse.RequestParser()
#         parser.add_argument('id', type=int, help='Yada Yada Yada')
#         parser.add_argument('location', type=str, help='Yada Yada Yada')
#         args = parser.parse_args()
#         account_id = args['id']
#         location = args['location']

#         if not location or not account_id:
#             return {"status": 400, "message": "Missing arguments.(?id=&location=)"}

#     	events_sim = events_sim_with_loc(account_id, location, EVENT_TYPES_URI)
#         update_events_table(account_id, events_sim)
#         return {"status": 200, "data": events_sim.to_json(orient='records')}

# @similarity_api.resource('/sim/i/<int:id>')
# class InterestSimilarityAPI(Resource):
#     @staticmethod
#     def get(id):
#     	return interests_sim(id).to_json(orient='records')

# @similarity_api.resource('/similarity/interets')
# class SocialInterestSimilarityAPI(Resource):
#     @staticmethod
#     def get():
#         parser = reqparse.RequestParser()
#         parser.add_argument('id', type=int, help='Yada Yada Yada')
#         parser.add_argument('location', type=str, help='Yada Yada Yada')
#         parser.add_argument('type', type=str, help='Yada Yada Yada')
#         args = parser.parse_args()
#         account_id = args['id']
#         location = args['location']
#         interest_type = args['type']

#         if not account_id or not location or not interest_type:
#             return {"status": 400, "message": "Missing arguments.(?id=&type=&location=)"}

#         if interest_type == INTEREST_TYPES['SOCIAL']:
#             URI = SOCIAL_INTERESTS_URI
#         elif interest_type == INTEREST_TYPES['BUSINESS']:
#             URI = BUSINESS_INTERESTS_URI
#         elif interest_type == INTEREST_TYPES['LIFESTYLE']:
#             URI = LIFESTYLE_INTERESTS_URI
#         else:
#             return {"status": 400, "message": "Missing interest type(?type=)."}

#         interests_sim = interests_sim_with_loc(account_id, location, URI)
#         update_interests_table(account_id, interests_sim, interest_type)
#     	return {"status": 200, "data": interests_sim.to_json(orient='records')}

@similarity_api.resource('/similarity/interets')
class SocialInterestSimilarityAPI(Resource):
    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, help='Account id is required.')
        args = parser.parse_args()
        account_id = args['id']

        params = {
            'id': account_id,
            'location': False,
            'chapter': True,
            'nationality': False
        }

        process_single_interest_similarity(SOCIAL_INTERESTS_URI, INTEREST_TYPES['SOCIAL'], params)
        # return {"status": 200, "data": interests_sim.to_json(orient='records')}

