import logging
import boto3
from botocore.exceptions import ClientError

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add a handler to ensure the log messages are displayed
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)

class SNSManager:
    def __init__(self):
        self.sns_resource = boto3.resource('sns')
    
    def create_topic(self, name='BudgetAlerts'):
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
            print(f"Created Topic ARN: {topic.arn}")
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic

# Example usage
if __name__ == "__main__":
    sns_manager = SNSManager()
    sns_manager.create_topic('BudgetAlerts')  