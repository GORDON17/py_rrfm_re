import sys
from apscheduler.schedulers import SchedulerNotRunningError
from flask import Blueprint, json, jsonify, request
from flask_restful import Api, Resource, reqparse

from services.job_service import *
from services.mongodb import *
from configurations.env_configs import *
from configurations.constants import *
from api import check_token

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
# sched = Scheduler(s)

job_api = Api(Blueprint('job_api', __name__))

@job_api.resource("/runscheduler/generate")
class JobGenerateAPI(Resource):
    @staticmethod
    def post():
			parser = reqparse.RequestParser()
			parser.add_argument('day', type=int, help='Day cannot be blank!')
			parser.add_argument('hour', type=int, help='Hour cannot be blank!')
			parser.add_argument('minute', type=int, help='Minute cannot be blank!')
			args = parser.parse_args()
			day = args['day']
			hour = args['hour']
			minute = args['minute']

			if not check_token(parser):
				return {'status': 403, 'message': 'Permission Denied'}

			json_data = request.get_json(force=True)
			print "Setup a generate scheduler at: ", (day, hour, minute)

			try:
				# global sched
				global scheduler

				params = {
					'location': json_data['location'],
					'chapter': json_data['chapter'],
					'nationality': json_data['nationality']
				}

				scheduler.add_job(g_social_interest_similarity_job, 'cron', args=[params],
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='0',
												name=JOB['GENERATE']['SOCIAL_INTEREST_SIMILARITY'])
				scheduler.add_job(g_mutual_friends_job, 'cron', args=[params],
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='1',
												name=JOB['GENERATE']['MUTUAL_FRIEND'])
				scheduler.start()
				# sched.schedule_jobs(day_of_week=2, hour=9, minute=33)
				# sched.start()
				return {'status': 200, 'message': 'The scheduler is running.'}
			except:
				print sys.exc_info()[0]
				return {'status': 400, 'message': 'The scheduler is failed to start.'}


@job_api.resource("/runscheduler/retrieve")
class JobRetrieveAPI(Resource):
    @staticmethod
    def post():
			parser = reqparse.RequestParser()
			parser.add_argument('day', type=int, help='Day cannot be blank!')
			parser.add_argument('hour', type=int, help='Hour cannot be blank!')
			parser.add_argument('minute', type=int, help='Minute cannot be blank!')
			args = parser.parse_args()
			day = args['day']
			hour = args['hour']
			minute = args['minute']

			if not check_token(parser):
				return {'status': 403, 'message': 'Permission Denied'}

			print "Setup a retrieve scheduler at: ", (day, hour, minute)

			try:
				global scheduler

				scheduler.add_job(r_interest_similarity_job, 'cron',
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='0',
												name=JOB['RETRIEVE']['SOCIAL_INTEREST_SIMILARITY'])
				scheduler.add_job(r_mutual_friend_job, 'cron',
												day_of_week=day, 
												hour=hour, 
												minute=minute,
												id='1',
												name=JOB['RETRIEVE']['MUTUAL_FRIEND'])

				scheduler.start()
				return {'status': 200, 'message': 'The scheduler is running.'}
			except:
				print sys.exc_info()[0]
				return {'status': 400, 'message': 'The scheduler is failed to start.'}


@job_api.resource("/stopscheduler")
class JobStopAPI(Resource):
    @staticmethod
    def get():
			parser = reqparse.RequestParser()
			if not check_token(parser):
				return {'status': 403, 'message': 'Permission Denied'}

			try:
				scheduler.shutdown(wait=False)
				return {'status': 200, 'message': 'The scheduler is shutdown.'}
			except SchedulerNotRunningError, e:
				return {'status': 400, 'message': str(e)}

@job_api.resource("/list")
class JobListAPI(Resource):
    @staticmethod
    def get():
			parser = reqparse.RequestParser()
			if not check_token(parser):
				return {'status': 403, 'message': 'Permission Denied'}

			try:
				data = get_jobs()
				return {'status': 200, 'message': 'OK', 'data': data }
			except:
				return {'status': 400, 'message': 'Could not retrieve job list.'}





