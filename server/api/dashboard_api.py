from flask_restful import Api, Resource, reqparse
from flask import Blueprint, json, jsonify

from services.dashboard_service import *
from configurations.env_configs import *
from api import check_token

dashboard_api = Api(Blueprint('dashboard_api', __name__))

@dashboard_api.resource("/month-count")
class MonthCount(Resource):
	@staticmethod
	def get():
		parser = reqparse.RequestParser()
		if not check_token(parser):
			return {'status': 403, 'message': 'Permission Denied'}

		return getMonthCount(MONTH_COUNT_URI)
		