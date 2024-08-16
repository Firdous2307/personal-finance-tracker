# AWS SNS Integration Issue

## Problem:
The application relies on AWS SNS to send notifications, which requires AWS credentials. When users fork the repo and run the program, it fails because the AWS credentials are not configured for them.


## Cause:
AWS SNS operations in `aws_sns.py` require valid AWS credentials. These credentials are specific to your AWS account and are not included in the repository for security reasons. Users forking the repo will need to set up their own credentials.


1. Set Up AWS Credentials:

Users must configure their AWS credentials using one of the following methods:

Update your `aws_sns.py` to check if credentials are present and guide users on how to set them up.

```python
import os
import logging
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class SNSManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        try:
            self.sns_client = boto3.client('sns')
            self.sns_resource = boto3.resource('sns')
            self.topic_arn = load_aws_sns_topic_arn()
        except (NoCredentialsError, PartialCredentialsError) as e:
            self.logger.error("AWS credentials are not configured properly: %s", e)
            raise
```

**AWS CLI:** Run aws configure in the terminal and provide your AWS Access Key, Secret Key, and region.

**Environment Variables:** Set the following environment variables in your terminal or .env file:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_region
```

Alternatively, users can create an AWS credentials file at ~/.aws/credentials.

2. Local Mode (No AWS):

If you don’t have AWS credentials, the program can run in **local mode** where AWS SNS features are disabled. You’ll be prompted to choose this mode when running the application.


```python
class SNSManager:
    def __init__(self, use_sns=True):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

        if use_sns:
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

```


## Conditional Alerts Setup in main.py

Modify `main.py` to allow running without AWS SNS if credentials are not set.

```python
def main():
    use_sns = input("Do you want to enable AWS SNS alerts? (yes/no): ").strip().lower() == 'yes'
    sns_notifier = SNSNotifier() if use_sns else None

    # Rest of the code...
    if sns_notifier:
        sns_notifier.setup()
```