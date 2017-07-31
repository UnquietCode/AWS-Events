import os
import json
import boto3

sns = boto3.client('sns')
sts = boto3.client('sts')


def publish_event(source, subject=None, message=None, data=None):
    subject = subject or ''
    message = message or ''

    message_data = json.dumps({
        'email': message,
        'sms': subject,
        'default': json.dumps({
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
    
    
def send_sms(sender, recipients, text):
    last_exception = None
    
    for recipient in recipients:
        try:
            sns.publish(
                PhoneNumber=recipient,
                Message=text,
                MessageAttributes={
                    'AWS.SNS.SMS.SenderID': {
                        'DataType': 'String',
                        'StringValue': sender or 'AWS'
                    },
                    'AWS.SNS.SMS.SMSType': {
                        'DataType': 'String',
                        'StringValue': 'Transactional'
                    },
                    'AWS.SNS.SMS.MaxPrice': {
                        'DataType': 'Number',
                        'StringValue': '0.10'
                    }
                }
            )
        except Exception as e:
            print(e)
            last_exception = e
    
    if len(recipients) <= 1:
        if last_exception is not None:
            raise last_exception
        