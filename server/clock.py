import os
from configurations.constants import JOB
from services.job_service import *

from apscheduler.schedulers.background import BlockingScheduler

scheduler = BlockingScheduler()
# hour_offset_6 = int(os.environ.get('G_HOUR')) + 6

"""
# day_of_week=os.environ.get('G_DAY'), 
@scheduler.scheduled_job('cron', hour=os.environ.get('G_HOUR'), minute=os.environ.get('G_MINUTE'), id='01', name=JOB['GENERATE']['ALL_INTEREST_SIMILARITY'])
def all_interest_similarity_job_with_lcn():
	params = {
		'location': False,
		'chapter': True,
		'nationality': False
	}
	try:
		print "all_interest_similarity_job_with_lcn is running."
		g_all_interest_similarity_job(params)
	except:
		print "all_interest_similarity_job_with_lcn is failed!"

# day_of_week=os.environ.get('G_DAY'), 
@scheduler.scheduled_job('cron', hour=os.environ.get('G_HOUR_OFFSET'), minute=os.environ.get('G_MINUTE'), id='02', name=JOB['GENERATE']['MUTUAL_FRIEND'])
def mutual_friend_job_with_lcn():
	params = {
		'location': False,
		'chapter': True,
		'nationality': False
	}
	try:
		print "mutual_friend_job_with_lcn is running."
		g_mutual_friends_job(params)
	except:
		print "mutual_friend_job_with_lcn is failed!"

# day_of_week=os.environ.get('R_DAY'), 

@scheduler.scheduled_job('cron', hour=os.environ.get('R_HOUR'), minute=os.environ.get('R_MINUTE'), id='11', name=JOB['RETRIEVE']['ALL_INTEREST_SIMILARITY'])
def interest_similarity_sqs_job():
	try:
		print "interest_similarity_sqs_job is running."
		r_interest_similarity_job()
	except:
		print "interest_similarity_sqs_job is failed!"

# day_of_week=os.environ.get('R_DAY'), 
@scheduler.scheduled_job('cron', hour=os.environ.get('R_HOUR_OFFSET'), minute=os.environ.get('R_MINUTE'), id='12', name=JOB['RETRIEVE']['MUTUAL_FRIEND'])
def mutual_friend_sqs_job():
	try:
		print "mutual_friend_sqs_job is running."
		r_mutual_friend_job()
	except:
		print "mutual_friend_sqs_job is failed!"

"""

@scheduler.scheduled_job('cron', hour=os.environ.get('G_HOUR'), minute=os.environ.get('G_MINUTE'), id='01', name="all_jobs")
def all_jobs():
	params = {
		'location': False,
		'chapter': True,
		'nationality': False
	}
	try:
		print "all_jobs is running."
		run_all_jobs(params)
	except:
		print "all_jobs is failed!"

@scheduler.scheduled_job('cron', hour=os.environ.get('R_HOUR'), minute=os.environ.get('R_MINUTE'), id='02', name="restart_heroku")
def restart_heroku():
	restart_heroku()

scheduler.start()