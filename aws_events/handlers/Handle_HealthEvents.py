from utils import publish_event


def get_event_description(event):
    descriptions = {
        x['language']: x['latestDescription']
        for x in event['detail']['eventDescription']
    }
    return descriptions['en_US']


def handler(event, context):
    print(event)

    subject = event['detail-type']
    message = get_event_description(event)
    
    publish_event(
        source='PersonalHealthDashboard',
        subject=subject,
        message=message,
        data={
            'resources': event['resources'],
            'details': event['detail'],
        }
    )