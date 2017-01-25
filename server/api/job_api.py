from apscheduler.schedulers import SchedulerNotRunningError
from flask import Blueprint, json, jsonify
from flask_restful import Api, Resource, reqparse

from services.job_service import *
from services.mongodb import get_jobs
from configurations.env_configs import *

from apscheduler.schedulers.background import BackgroundScheduler

s = BackgroundScheduler()
# sched = Scheduler(s)

job_api = Api(Blueprint('job_api', __name__))

@job_api.resource("/runsched")
class JobStartAPI(Resource):
    @staticmethod
    def get():
			parser = reqparse.RequestParser()
			parser.add_argument('day', type=int, help='Yada Yada Yada')
			parser.add_argument('hour', type=int, help='Yada Yada Yada')
			parser.add_argument('minute', type=int, help='Yada Yada Yada')
			args = parser.parse_args()
			day = args['day']
			hour = args['hour']
			minute = args['minute']
			print(day, hour, minute)
			try:
				# global sched
				global s
				s.add_job(interest_similarity_job, 'cron', 
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='0',
												name='social_interest_similarity')
				s.add_job(mutual_friends_job, 'cron', 
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='1',
												name='mutual_friend')
				s.start()
				# sched.schedule_jobs(day_of_week=2, hour=9, minute=33)
				# sched.start()
				return {'status': 200, 'message': 'The scheduler is running.'}
			except:
				return {'status': 400, 'message': 'The scheduler is failed to start.'}


@job_api.resource("/stopsched")
class JobStopAPI(Resource):
    @staticmethod
    def get():
			try:
				s.shutdown(wait=False)
				return {'status': 200, 'message': 'The scheduler is shutdown.'}
			except SchedulerNotRunningError, e:
				return {'status': 400, 'message': str(e)}

@job_api.resource("/jobs")
class JobListAPI(Resource):
    @staticmethod
    def get():
			try:
				return get_jobs()
			except:
				return {'status': 400, 'message': 'Could not retrieve job list.'}




