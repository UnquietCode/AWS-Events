import os
import json

from utils import post_json

# grab the webhook URL from the environment
URL = os.environ['SlackURL']


def notify_channel(channel, name, icon, text, data):
    print('posting to '+channel)
    
    attachments = [{
        'fallback': text,
        'pretext': text,
        'mrkdwn_in': ['pretext'],
    }]
    
    data = data or {}
    
    for key, value in data.items():
        if isinstance(value, dict):
            data_string = json.dumps(value, indent=2)
            data_string = "```\n{}\n```".format(data_string)
        else:
            data_string = value
        
        attachments.append({
            'title': key,
            'fallback': key,
            'color': 'warning',
            'text': data_string,
            'mrkdwn_in': ['text'],
        })
    
    payload = {
        'username': name,
        'icon_emoji': icon,
        'channel': channel,
        'attachments': attachments,
    }
    
    post_json(URL, payload)


def handler(event, context):
    print(event)
    
    # allow one or many channels, but not both
    if 'channel' in event and 'channels' in event:
        raise Exception('provide one or many channels, but not both')
    
    channels = event.get('channels', [])
    
    if 'channel' in event:
        channels.append(event['channel'])

    name = event.get('name', 'AWS')
    icon = event.get('icon', ':heavy_check_mark:')
    text = event.get('text', '')
    data = event.get('data')
    
    for channel in channels:
        notify_channel(channel, name, icon, text, data)