import json
from utils import publish_event


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = json.loads(message_content['Message'])
    print(message_data)
    
    # sanity check
    if len(message_data) != 1:
        raise Exception('expected a single key/value pair')
    
    # extract the only key and value
    event_key, event_source = list(message_data.items())[0]
    
    # remove the 'ElastiCache:' portion
    event_name = event_key.split(':')[1]
    
    # put spaces between capital letters
    event_name = " ".join(event_name.split('(?=[A-Z])'))

    subject = "cache event in {}".format(event_source)
    message = "{} in cluster {}.".format(event_name, event_source)

    publish_event(
        source='ElastiCache',
        subject=subject,
        message=message,
        data={
            'event_name': event_name,
            'cache_cluster': event_source,
            'details': message_data,
        }
    )