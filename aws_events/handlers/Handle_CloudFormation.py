import re
from utils import publish_event


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
    stack_name = message_data['StackName']
    
    message = "Stack '{}' has entered state '{}'.".format(
        stack_name,
        status,
    )

    publish_event(
        source='CloudFormation',
        subject='CloudFormation Event',
        message=message,
        data={
            'status': status,
            'stack_name': stack_name,
            'details': message_data,
        }
    )