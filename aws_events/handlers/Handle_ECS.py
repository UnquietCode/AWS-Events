from utils import publish_event


def get_event_description(event):
    event_type = event['detail-type']
    
    if 'ECS Task State Change' == event_type:
        from_state = event['detail']['lastStatus']
        to_state = event['detail']['desiredStatus']
        description = "transitioning from state {} to {}".format(from_state, to_state)
    else:
        description = 'AWS ECS Event'

    return description


def handler(event, context):
    print(event)

    subject = event['detail-type']
    message = get_event_description(event)
    
    publish_event(
        source='ECS',
        subject=subject,
        message=message,
        data={
            'details': event['detail'],
        }
    )