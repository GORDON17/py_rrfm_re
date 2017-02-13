from flask_restful import Api, Resource, reqparse
from flask import Blueprint, json, jsonify

from services.dashboard_service import *
from configurations.env_configs import *

dashboard_api = Api(Blueprint('dashboard_api', __name__))

@dashboard_api.resource("/month-count")
class MonthCount(Resource):
	@staticmethod
	def get():
		return getMonthCount(MONTH_COUNT_URI)
		