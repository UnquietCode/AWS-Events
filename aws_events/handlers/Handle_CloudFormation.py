import re
from utils import publish_event

IGNORED_STATUSES = [
    'UPDATE_COMPLETE_CLEANUP_IN_PROGRESS'
]

def parse_message(message):
    data = {}

    for match in re.findall("(.+)='(.*)'", message):
        name = match[0]
        value = match[1]
        data[name] = value
        
    return data


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = parse_message(message_content['Message'])
    print(message_data)

    # skip individual resource update events
    if message_data['ResourceType'] != 'AWS::CloudFormation::Stack':
        print('skipping non-stack resource')
        return

    status = message_data['ResourceStatus']
    
    # skip statuses we don't care about
    if status in IGNORED_STATUSES:
        print("skipping ignored status '{}'".format(status))
        return
    
    message = "Stack '{}' has entered state '{}'.".format(
        message_data['LogicalResourceId'],
        status,
    )

    publish_event(
        source='CloudFormation',
        subject='CloudFormation Event',
        message=message,
        data=message_data,
    )