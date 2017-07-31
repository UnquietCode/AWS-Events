import os
import json

from utils.sns_helpers import send_sms


# grab the sender ID from the environment
SenderID = os.environ['SenderPhoneID']


def handler(event, context):
    print(event)
    
    # allow one or recipients, but not both
    if 'recipient' in event and 'recipients' in event:
        raise Exception('provide one or many recipients, but not both')
    
    recipients = event.get('recipients', [])
    
    if 'recipient' in event:
        recipients.append(event['recipient'])
    
    text = event['text']
    
    send_sms(
        sender=SenderID,
        recipients=recipients,
        text=text,
    )