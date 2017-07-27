import json
from utils import publish_event


def handler(event, context):
    message_content = event['Records'][0]['Sns']
    message_data = json.loads(message_content['Message'])
    print(message_data)

    event_message = message_data.get('Event Message', '')
    database_name = message_data['Source ID']
    database_url = message_data['Identifier Link']
    
    eventID = message.get('Event ID', '').strip()
    last_hash = eventID.rfind('#')
    event_name = eventID[lastHash+1, -1] if last_hash > 0 else '???'
    
    message = "{}\n{}\n\nSee {} for more information.".format(
        event_message,
        database_url,
        eventID,
    )

    publish_event(
        source='RDS',
        subject='Database Event',
        message=message,
        data={
            'event_name': event_name,
            'database_name': database_name,
            'details': message_data
        }
    )