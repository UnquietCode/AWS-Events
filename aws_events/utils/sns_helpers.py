import os
import json
import boto3

sns = boto3.client('sns')
sts = boto3.client('sts')


def publish_event(source, subject=None, message=None, data=None):
    subject = subject or ''
    message = message or ''

    message_data = json.dumps({
        'default': message,
        'email': message,
        'sms': subject,
        'json': json.dumps({
            'source': source,
            'subject': subject,
            'message': message,
            'data': data,
        }),
    })
    
    region = os.environ['AWS_DEFAULT_REGION']
    account = sts.get_caller_identity()['Account']
    topic_arn = "arn:aws:sns:{}:{}:{}".format(region, account, 'Receive_Events')
    
    sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message_data,
        MessageStructure='json',
    )