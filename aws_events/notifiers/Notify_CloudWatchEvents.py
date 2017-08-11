from utils.cloudwatch_helpers import put_event


def handler(event, context):
    print(event)
    
    event_type = event['type']
    resources = event.get('resources', [])
    details = event.get('details', None)
    
    put_event(
        source='uqc.aws-events',
        event_type=event_type,
        resources=resources,
        details=details,
    )