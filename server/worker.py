import os
from configurations.constants import JOB
from services.job_service import *

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

params = {
    'location': False,
    'chapter': True,
    'nationality': False
}

hour=os.environ.get('G_HOUR')
minute=os.environ.get('G_MINUTE')

scheduler.add_job(g_all_interest_similarity_job, 
                    'cron', 
                    args=[params],
                    hour=hour, 
                    minute=minute,
                    id='0',
                    name=JOB['GENERATE']['ALL_INTEREST_SIMILARITY'])

scheduler.start()


