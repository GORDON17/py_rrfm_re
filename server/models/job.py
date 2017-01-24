from mongoengine import *

class Job(DynamicDocument):
	job_id = StringField(required=True)
	name = StringField(required=True)
	state = IntField(default=0)
	duration = IntField(default=0)
	created_at = DateTimeField(required=True)
	ended_at = DateTimeField()

	def to_json(self):
		return {
			'job_id': self.job_id,
			'name': self.name,
			'state': self.state,
			'duration': self.duration,
			'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),#.isoformat()
			'ended_at': self.ended_at.strftime("%Y-%m-%d %H:%M:%S")
		}