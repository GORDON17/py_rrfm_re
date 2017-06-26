import os
from configurations.constants import JOB
from services.job_service import *


from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler({
    'apscheduler.jobstores.mongo': {
         'type': 'mongodb'
    },
    'apscheduler.jobstores.default': {
        'type': 'mongodb',
        'url': os.environ.get('MONGO_URL')
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '10'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '4'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
})

@scheduler.scheduled_job('cron', hour=os.environ.get('G_HOUR'), minute=os.environ.get('G_MINUTE'), id='01', name=JOB['GENERATE']['ALL_INTEREST_SIMILARITY'])
def all_interest_similarity_job_with_lcn():
	params = {
		'location': False,
		'chapter': True,
		'nationality': False
	}
	try:
		print "all_interest_similarity_job_with_lcn is running."
		mp_process_all_interest_similarity(params)
	except:
		print "all_interest_similarity_job_with_lcn is failed!"




