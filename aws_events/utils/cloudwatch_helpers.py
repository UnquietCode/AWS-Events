import json
import boto3

cw_events = boto3.client('events')


def put_event(source, event_type, resources, details):
    resources = resources or []
    details = json.dumps(details) if details else '{}'
    
    cw_events.put_events(Entries=[
        {
            'Source': source,
            'DetailType': event_type,
            'Resources': resources,
            'Detail': details,
        }
    ])