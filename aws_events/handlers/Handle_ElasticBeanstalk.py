import re
from utils import publish_event


def parse_message(message):
    data = {}

    for match in re.findall('^(.+?): (.*)$', message, re.MULTILINE):
        name = match[0]
        value = match[1]
        data[name] = value
        
    return data


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = parse_message(message_content['Message'])
    print(message_data)
    
    subject = message_content.get('Subject', 'ElasticBeanstalk Event')
    message = message_data.get('Message', '')
    
    publish_event(
        source='ElasticBeanstalk',
        subject=subject,
        message=message,
        data={
            'application_name': message_data['Application'],
            'environment_name': message_data['Environment'],
            'details': message_data,
        }
    )