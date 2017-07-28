import os
import json

from utils.ses_helpers import send_email


# grab the sender email address from the environment
SenderEmailAddress = os.environ['SenderEmailAddress']


def handler(event, context):
    print(event)
    
    # allow one or recipients, but not both
    if 'recipient' in event and 'recipients' in event:
        raise Exception('provide one or many recipients, but not both')
    
    recipients = event.get('recipients', [])
    
    if 'recipient' in event:
        recipients.append(event['recipient'])
    
    subject = event['subject']
    text = event['text']
    data = event.get('data', {})

    # build some html
    sections = []

    for key, value in data.items():
        data_string = json.dumps(value, indent=2)
        html_string = "<h3>{}</h3><pre>{}</pre>".format(key, data_string)
        sections.append(html_string)
    
    html = "<html><body>\n<p>{}</p>\n{}</body></html>".format(
        text, '\n'.join(sections)
    )

    send_email(
        sender=SenderEmailAddress,
        recipients=recipients,
        subject=subject,
        text=text,
        html=html,
    )