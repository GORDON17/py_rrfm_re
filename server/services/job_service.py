# from services.mongodb import connect_db
# connect_db()

import time

from services.similarity_service import process_interest_similarity
from services.mongodb import *
from services.bfs_service import process_mutual_friends

from configurations.env_configs import *
from configurations.development import *
from configurations.constants import *

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


from multiprocessing import Process


# class Scheduler:
# 	def __init__(self, sched):
# 		self.sched = sched

# 	def schedule_jobs(self, day_of_week, hour, minute):
# 		self.sched.add_job(self.interest_similarity_job, 'cron', 
# 												day_of_week=day_of_week, 
# 												hour=hour, 
# 												minute=minute,
# 												id='0',
# 												name='social_interest_similarity')
# 		self.sched.add_job(self.mutual_friends_job, 'cron', 
# 												day_of_week=day_of_week, 
# 												hour=hour, 
# 												minute=minute,
# 												id='1',
# 												name='mutual_friend')
# 		# self.sched.start()

# 	def start(self):
# 		self.sched.start()
# 		self.sched.print_jobs()

# 	def print_jobs(self):
# 		self.sched.print_jobs()	

# 	def shutdown(self, wait=False):
# 		self.sched.shutdown(wait=wait)
# 		self.sched.remove_all_jobs()

# 	def interest_similarity_job(self):
# 		p = Process(target=mp_process_interest_similarity, args=())
# 		p.start()

# 	def mp_process_interest_similarity(self):
# 		connect_db()
# 		job_id = '0'
# 		job_name = 'social_interest_similarity'
# 		print('social_interest_similarity job is pendding.')

# 		job_obj_id = add_job(job_id=job_id, name=job_name)
		
# 		print('social_interest_similarity job is running.')
# 		process_interest_similarity(SOCIAL_INTERESTS_URI, INTEREST_TYPES['social'])

# 		if job_obj_id:
# 			update_job_state(job_obj_id=job_obj_id, state=1)
# 			print('social_interest_similarity job is finished.')
# 		else:
# 			print('there is no such job')


# 	def mutual_friends_job(self):
# 		p = Process(target=mp_process_mutual_friends, args=())
# 		p.start()

# 	def mp_process_mutual_friends():
# 			connect_db()
# 			job_id = '1'
# 			job_name = 'mutual_friend'
# 			print('mutual_friend job is pendding.')

# 			job_obj_id = add_job(job_id=job_id, name=job_name)
			
# 			print('mutual_friend job is running.')
# 			process_mutual_friends(CONNECTIONS_URI)

# 			if job_obj_id:
# 				update_job_state(job_obj_id=job_obj_id, state=1)
# 				print('mutual_friend job is finished.')
# 			else:
# 				print('there is no such job')




# sched = BackgroundScheduler()
# day_of_week = 1
# job_hour = 15
# job_minute = 38

# @sched.scheduled_job('cron', day_of_week=day_of_week, hour=job_hour, minute=job_minute, id='0', name='social_interest_similarity')
# def scheduled_job():
# 		p = Process(target=mp_process_interest_similarity, args=())
# 		p.start()

def g_all_interest_similarity_job(params):
		p = Process(target=mp_process_all_interest_similarity, args=(params,))
		p.start()

def mp_process_all_interest_similarity(params):
		connect_db()
		job_id = '0'
		job_name = JOB['GENERATE']['ALL_INTEREST_SIMILARITY']
		print('g_all_interest_similarity job is pendding.')

		job_obj_id = add_job(job_id=job_id, name=job_name)
		
		print('g_all_interest_similarity job is running.')
		drop_interest_similarity_collection()
		process_interest_similarity(SOCIAL_INTERESTS_URI, INTEREST_TYPES['SOCIAL'], params)
		# process_interest_similarity(BUSINESS_INTERESTS_URI, INTEREST_TYPES['BUSINESS'], params)
		# process_interest_similarity(LIFESTYLE_INTERESTS_URI, INTEREST_TYPES['LIFESTYLE'], params)

		if job_obj_id:
			update_job_state(job_obj_id=job_obj_id, state=1)
			print('g_all_interest_similarity job is finished.')
		else:
			print('there is no such job')

# @sched.scheduled_job('cron', day_of_week=day_of_week, hour=job_hour, minute=job_minute, id='1', name='mutual_friend')
# def scheduled_job():
# 		p = Process(target=mp_process_mutual_friends, args=())
# 		p.start()

def g_mutual_friends_job(params):
		p = Process(target=mp_generate_mutual_friends, args=(params,))
		p.start()

def mp_generate_mutual_friends(params):
		connect_db()
		job_id = '1'
		job_name = JOB['GENERATE']['MUTUAL_FRIEND']
		print('g_mutual_friend job is pendding.')

		job_obj_id = add_job(job_id=job_id, name=job_name)
		
		print('g_mutual_friend job is running.')
		drop_mutual_friend_collection()
		process_mutual_friends(CONNECTIONS_URI, params)

		if job_obj_id:
			update_job_state(job_obj_id=job_obj_id, state=1)
			print('g_mutual_friend job is finished.')
		else:
			print('there is no such job')


from services.sqs_service import *
SIZE = 100
import os
import heroku3
heroku_conn = heroku3.from_key(os.environ.get('HEROKU_KEY'))
heroku_app = heroku_conn.apps()[os.environ.get('APP_NAME')]

def r_interest_similarity_job():
	p = Process(target=mp_retrieve_interest_similarity)
	p.start()

def mp_retrieve_interest_similarity():
	print "Sending interest similarity intros to Vault ..."
	vaults = build_interest_recommendation_vault_objects()
	print "Total vault objects: ", len(vaults)
	sqs = SQSService()

	count = 1
	for i in xrange(0, len(vaults), SIZE):
		sqs.push_objects_into_vault(vaults[i:i + SIZE])
		count += 1
	print "Total batch sent: ", count


def r_mutual_friend_job():
	p = Process(target=mp_retrieve_mutual_friend)
	p.start()

def mp_retrieve_mutual_friend():
	print "Sending mutual intros to Vault ..."
	vaults = build_mutual_recommendation_vault_objects()
	print "Total vault objects: ", len(vaults)
	sqs = SQSService()

	count = 1
	for i in xrange(0, len(vaults), SIZE):
		sqs.push_objects_into_vault(vaults[i:i + SIZE])
		count += 1
	print "Total batch sent: ", count
	heroku_app.restart()


def run_all_jobs(params):
	p = Process(target=mp_all_jobs, args=(params,))
	p.start()

def mp_all_jobs(params):
	mp_process_all_interest_similarity(params)
	mp_generate_mutual_friends(params)
	mp_retrieve_interest_similarity()
	mp_retrieve_mutual_friend()

def restart_heroku():
	heroku_app.restart()


# @sched.scheduled_job('interval', minutes=0.1, id='0', name='social_interest_similarity')
# def timed_job():
# 		job_id = '0'
# 		job_name = 'social_interest_similarity'
# 		print('social_interest_similarity job is pendding.')

# 		job_obj_id = add_job(job_id=job_id, name=job_name)
		
# 		print('social_interest_similarity job is running.')
# 		process_interest_similarity(SOCIAL_INTERESTS_URI)

# 		if job_obj_id:
# 			update_job_state(job_obj_id=job_obj_id, state=1)
# 			print('social_interest_similarity job is finished.')
# 		else:
# 			print('there is no such job')


# @sched.scheduled_job('interval', minutes=0.1, id='1', name='mutual_friend')
# def timed_job():
# 		job_id = '1'
# 		job_name = 'mutual_friend'
# 		print('mutual_friend job is pendding.')

# 		job_obj_id = add_job(job_id=job_id, name=job_name)
		
# 		print('mutual_friend job is running.')
# 		process_mutual_friends(CONNECTIONS_URI)

# 		if job_obj_id:
# 			update_job_state(job_obj_id=job_obj_id, state=1)
# 			print('mutual_friend job is finished.')
# 		else:
# 			print('there is no such job')




# @sched.scheduled_job('interval', minutes=0.2, id='1', name='interest_similarity')
# def timed_job():
# 		print('interest_similarity job is running.')
# 		events_sim = events_sim_with_loc(28071, 'New York', EVENT_TYPES_URI)
# 		print('interest_similarity: found similarity.......')
# 		update_events_table(28071, events_sim)



