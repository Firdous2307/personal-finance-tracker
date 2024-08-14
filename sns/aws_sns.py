import sys
import os
import logging
import boto3
from botocore.exceptions import ClientError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import AWS_SNS_TOPIC_ARN

class SNSManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        self.sns_client = boto3.client('sns')
        self.sns_resource = boto3.resource('sns')
        self.topic_arn = None
    
    def create_topic(self, name='BudgetAlerts'):
        try:
            topic = self.sns_resource.create_topic(Name=name)
            self.topic_arn = topic.arn 
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

    def send_alert(self, subject, message):
        if not self.topic_arn:
            raise ValueError("Topic ARN is not set. Please create a topic first.")
        try:
            response = self.sns_client.publish(
                TopicArn=self.topic_arn,
                Subject=subject,
                Message=message
            )
            self.logger.info(f"Alert sent: {response['MessageId']}")
            print(f"Alert sent: {response['MessageId']}")
        except ClientError:
            self.logger.exception("Couldn't send alert.")
            raise

        
class SNSNotifier:
    def __init__(self):
        self.manager = SNSManager()
    
    def setup(self):
        topic = self.manager.create_topic()
        self.manager.topic_arn = topic.arn
        self.manager.subscribe(topic, 'email', 'ayomilekanaraoye@gmail.com')

    def send_alert(self, subject, message):
        self.manager.send_alert(subject, message)

# Example usage
if __name__ == "__main__":
    sns_notifier = SNSNotifier()
    sns_notifier.setup()
    sns_notifier.send_alert("Test Alert", "This is a test message.")
