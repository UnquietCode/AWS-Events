import json
from utils import publish_event


def handler(event, context):
    message_data = json.loads(event['Records'][0]['Sns']['Message'])
    print(message_data)

    event_message = message_data.get('Event Message', '')
    database_name = message_data['Source ID']
    database_url = message_data['Identifier Link']
    
    eventID = message_data.get('Event ID', '').strip()
    last_hash = eventID.rfind('#')
    event_name = eventID[last_hash+1:] if last_hash > 0 else '???'
    
    subject = "Database Event - {}".format(database_name)
    
    message = "{}\n{}".format(
        event_message,
        database_url,
    )
    
    if eventID:
        message = message + "\n\nSee {} for more information.".format(eventID)

    publish_event(
        source='RDS',
        subject=subject,
        message=message,
        data={
            'event_name': event_name,
            'database_name': database_name,
            'details': message_data
        }
    )