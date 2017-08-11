from utils import publish_event


def get_generic_event_description(event):
    return 'AWS Event'


def get_health_event_description(event):
    descriptions = {
        x['language']: x['latestDescription']
        for x in event['detail']['eventDescription']
    }
    return descriptions['en_US']


def get_ecs_event_description(event):
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
    
    event_source = event['source']
    event_type = event['detail-type']
    
    if event_source == 'aws.health':
        message = get_health_event_description(event)
        source = 'PersonalHealthDashboard'
    
    elif event_source == 'aws.ecs':
        message = get_ecs_event_description(event)
        source = 'ECS'
    
    else:
        message = get_generic_event_description(event)
        source = 'CloudWatchEvents'
    
    publish_event(
        source=source,
        subject=event_type,
        message=message,
        data={
            'resources': event['resources'],
            'details': event['detail'],
        }
    )