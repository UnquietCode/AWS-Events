from aws_events.utils import Event, publish_event


def handler(event, context):
    publish_event(
        source='CloudFormation',
        subject='SUBJECTT',
        message='MESSAGEE',
    )
    
    return 'OK'