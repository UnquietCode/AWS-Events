import json
from utils import post_json

URL = "https://hooks.slack.com/services/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"


def notify_channel(channel, name, icon, text, data):
    print('posting to '+channel)
    
    attachments = [{
        'fallback': text,
        'pretext': text,
        'mrkdwn_in': ['pretext'],
    }]
    
    data = data or {}
    
    for key, value in data.items():
        attachments.append({
            'title': key,
            'fallback': key,
            'color': 'warning',
            'text': "```\n{}\n```".format(json.dumps(value)),
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