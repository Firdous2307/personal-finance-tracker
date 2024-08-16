import sys
import os
import logging
import boto3
# For Local Use
from botocore.exceptions import ClientError
# for AWS Credentials, Uncomment for Use
#from botocore.exceptions import NoCredentialsError, PartialCredentialsError


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import load_aws_sns_topic_arn

class SNSManager:
       #def __init__(self):   # For AWS Credentials, uncomment for use

    def __init__(self, use_sns=True): # For Local Use
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        if use_sns: # Comment if you want to use AWS Credentials
            try:
                self.sns_client = boto3.client('sns')
                self.sns_resource = boto3.resource('sns')
                self.topic_arn = load_aws_sns_topic_arn()
            except (NoCredentialsError, PartialCredentialsError) as e:
                self.logger.error("AWS credentials are not configured properly: %s", e)
                raise
        else:
            self.logger.info("Running in local mode, SNS features disabled.")
            self.sns_client = None
            self.sns_resource = None
            self.topic_arn = None

    
    def create_topic(self, name='BudgetAlerts'):
        try:
            topic = self.sns_resource.create_topic(Name=name)
            self.topic_arn = topic.arn
            return topic
        except ClientError:
            self.logger.exception("Couldn't create topic %s.", name)
            raise

    def subscribe(self, topic, protocol, endpoint):
        try:
            subscription = topic.subscribe(
                Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True
            )
            return subscription
        except ClientError:
            self.logger.exception(
                "Couldn't subscribe %s %s to topic %s.", protocol, endpoint, topic.arn
            )
            raise

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
        except ClientError:
            self.logger.exception("Couldn't send alert.")
            raise

class SNSNotifier:
    def __init__(self):
        self.manager = SNSManager()
    
    def setup(self, email):
        try:
            topic = self.manager.create_topic()
            self.manager.subscribe(topic, 'email', email)
            print("SNS topic setup complete.")
            print(f"Subscribed {email} to SNS Topic.")
        except Exception as e:
            print(f"Error during SNS setup: {e}")

    def send_alert(self, subject, message):
        self.manager.send_alert(subject, message)

# Example usage
if __name__ == "__main__":
    sns_notifier = SNSNotifier()
    sns_notifier.setup()
    sns_notifier.send_alert("Test Alert", "This is a test message.")
