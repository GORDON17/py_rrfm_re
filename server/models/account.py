from mongoengine import *

class Account(DynamicDocument):
	account_id = IntField(required=True)
	email = StringField(required=True)