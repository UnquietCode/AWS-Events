import boto3

ses = boto3.client('ses')


def send_email(sender, recipients, subject, text, html=None):
    
    # make up some html
    if not html:
        html = "<html><body><p>{}</p></body></html>".format(text)
    
    ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': recipients,
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'utf8'
            },
            'Body': {
                'Text': {
                    'Data': text,
                    'Charset': 'utf8'
                },
                'Html': {
                    'Data': html,
                    'Charset': 'utf8'
                }
            }
        }
    )