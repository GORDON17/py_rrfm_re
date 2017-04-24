import json
from boto3.session import Session

class SQSService:
	def __init__(self):
		self.session = Session(
            aws_access_key_id='AKIAIT6PK2JKCZJB22NA',
            aws_secret_access_key='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',
            region_name='us-east-1'
        )
		self.client = self.session.client('sqs')

	def push_objects_into_vault(self, objects):
		response = self.client.send_message(
			QueueUrl='https://sqs.us-east-1.amazonaws.com/445532067301/Vault',
			MessageBody=json.dumps(objects))
		print "Sent a vault queue: %s" % response['MessageId']