from utils import publish_event


def handler(event, context):
    publish_event(
        source='CloudFormation',
        subject='SUBJECTT',
        message='MESSAGEE',
    )
    
    return 'OK'