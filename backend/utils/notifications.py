import boto3
from django.conf import settings

class NotificationService:
    def __init__(self):
        self.sns_client = boto3.client(
            'sns',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION_NAME,
        )

    def send_notification(self, subject, message):
        response = self.sns_client.publish(
            TopicArn=settings.AWS_SNS_TOPIC_ARN,
            Subject=subject,
            Message=message,
        )
        return response