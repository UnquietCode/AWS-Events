import os
import boto3

from utils.ses_helpers import send_email


# grab the sender email address from the environment
SenderEmailAddress = os.environ['SenderEmailAddress']


def handler(event, context):
    print(event)
    
    if 'recipient' in event and 'recipients' in event:
        raise Exception('provide one or many recipients, but not both')
    
    recipients = event.get('recipients', [])
    
    if 'recipient' in event:
        recipients.append(event['recipient'])
    
    subject = event['subject']
    text = event['text']
    # html = event.get('html')
    data = event.get('data', {})

    sections = ""

    for key, value in data.items():
        data_string = json.dumps(value, indent=2)
        html_string = "<h2>{}</h2><pre>{}</pre>".format(key, data_string)
        sections = sections + "\n" + html_string
    
    html = "<html><body><p>{}</p>{}</body></html>".format(text, sections)

    send_email(
        sender=SenderEmailAddress,
        recipients=recipients,
        subject=subject,
        text=text,
        html=html,
    )