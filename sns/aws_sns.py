import sys
import os
import logging
import boto3
from botocore.exceptions import ClientError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import AWS_SNS_TOPIC_ARN

class SNSManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        self.sns_client = boto3.client('sns')
        self.sns_resource = boto3.resource('sns')
    
    def create_topic(self, name='BudgetAlerts'):
        try:
            topic = self.sns_resource.create_topic(Name=name)
            self.logger.info("Created topic %s with ARN %s.", name, topic.arn)
            print(f"Created Topic ARN: {topic.arn}")
        except ClientError:
            self.logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic

    def subscribe(self, topic, protocol, endpoint):
        try:
            subscription = topic.subscribe(
                Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True
            )
            self.logger.info("Subscribed %s %s to topic %s.", protocol, endpoint, topic.arn)
        except ClientError:
            self.logger.exception(
                "Couldn't subscribe %s %s to topic %s.", protocol, endpoint, topic.arn
            )
            raise
        else:
            return subscription

class SNSNotifier:
    def __init__(self):
        self.manager = SNSManager()
    
    def setup(self):
        topic = self.manager.create_topic()
        self.manager.subscribe(topic, 'email', 'ayomilekanaraoye@gmail.com')

# Example usage
if __name__ == "__main__":
    sns_notifier = SNSNotifier()
    sns_notifier.setup()
