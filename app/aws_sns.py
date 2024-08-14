/*
#from botocore.exceptions import ClientError
import logging
import boto3

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SNSNotifier:
    def __init__(self):
        self.sns_resource = boto3.resource('sns')
    
    def create_topic(self, name='BudgetAlerts'):
   