import json
from utils import publish_event


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = json.loads(message_content['Message'])
    print(message_data)

    subject = message_data['Event Message']
    subject = subject or message_content.get('Subject', 'RDS Event')
    
    message = "database '{}' -- {}\n{}\n\nSee {} for more information.".format(
        message_data['Source ID'],
        message_data['Event Message'],
        message_data['Identifier Link'],
        message_data['Event ID'],
    )
    
    publish_event(
        source='RDS',
        subject=subject,
        message=message,
        data=message_data,
    )