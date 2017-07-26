from utils import publish_event


def handler(event, context):
    publish_event(
        source='CloudWatch',
        subject='SUBJECTT',
        message='MESSAGEE',
    )