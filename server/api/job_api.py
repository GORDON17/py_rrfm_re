from apscheduler.schedulers import SchedulerNotRunningError
from flask import Blueprint, json, jsonify
from flask_restful import Api, Resource

from services.job_service import *
from configurations.env_configs import *

job_api = Api(Blueprint('job_api', __name__))

@job_api.resource("/runsched")
class JobStartAPI(Resource):
    @staticmethod
    def get():
			try:
				sched.start()
				return {'status': 200, 'message': 'The scheduler is running.'}
			except:
				return {'status': 400, 'message': 'The scheduler is failed to start.'}


@job_api.resource("/stopsched")
class JobStopAPI(Resource):
    @staticmethod
    def get():
			try:
				sched.shutdown(wait=True)
				return {'status': 200, 'message': 'The scheduler is shutdown.'}
			except SchedulerNotRunningError, e:
				return {'status': 400, 'message': str(e)}
			