# from services.mongodb import connect_db
# connect_db()

import time

from services.similarity_service import *
from services.mongodb import *

from configurations.env_configs import *
from configurations.development import *

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor




def sched_listener(event):
	print event

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}

sched = BackgroundScheduler(executors=executors)
# sched = BlockingScheduler()

# sched.add_listener(sched_listener)

@sched.scheduled_job('interval', minutes=0.1, id='0', name='event_type_similarity')
def timed_job():
		job_id = '0'
		job_name = 'event_type_similarity'
		print('event_type_similarity job is pendding.')

		job_obj_id = add_job(job_id=job_id, name=job_name)
		
		print('event_type_similarity job is running.')
		time.sleep(5)

		if job_obj_id:
			update_job_state(job_obj_id=job_obj_id, state=1)
			print('event_type_similarity job is stoped.')
		else:
			print('there is no such job')

# @sched.scheduled_job('interval', minutes=0.2, id='1', name='interest_similarity')
# def timed_job():
# 		print('interest_similarity job is running.')
# 		events_sim = events_sim_with_loc(28071, 'New York', EVENT_TYPES_URI)
# 		print('interest_similarity: found similarity.......')
# 		update_events_table(28071, events_sim)

# @sched.scheduled_job('cron', day_of_week='sat', hour=0, timezone='UTC-05:00', id=0, name='event_type_similarity')
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

