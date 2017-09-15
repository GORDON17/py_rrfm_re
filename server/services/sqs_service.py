import json
from boto3.session import Session
from configurations.env_configs import *

class SQSService(object):
	def __init__(self):
		super(SQSService, self).__init__()
		
		self.session = Session(
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SERET_ACCESS_KEY,
            region_name = AWS_REGION_NAME
        )
		self.client = self.session.client('sqs')

	def push_objects_into_vault(self, objects):
		print("Sending vault objects: ", objects)
		response = self.client.send_message(
			QueueUrl = SQS_QUEUE_URL,
			MessageBody = json.dumps(objects))
		print "Sent a vault queue: %s" % response['MessageId']