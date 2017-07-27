import json
from utils import publish_event


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = json.loads(message_content['Message'])
    subject = message_content.get('Subject', '')
    
    message = "Metric '{}' is in state '{}'".format(
        message_data['Trigger']['MetricName'],
        message_data['NewStateValue'],
    )
    
    publish_event(
        source='CloudWatch',
        subject=subject,
        message=message,
        data=message_data,
    )