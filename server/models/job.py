from mongoengine import *

class Job(DynamicDocument):
	job_id = StringField(required=True)
	name = StringField(required=True)
	state = IntField(default=0)
	duration = IntField(default=0)
	created_at = DateTimeField(required=True)