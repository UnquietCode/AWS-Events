from utils import publish_event


def handler(event, context):
    publish_event(
        source='RDS',
        subject='SUBJECTT',
        message='MESSAGEE',
    )