import json
from zoomus import ZoomClient

API_KEY = 'zXu0oEg3Q46Brj0UbbNluA'
API_SECRET = 'qCP3qsKB4RtCvwmLCWyrRrenqt0l1nUvvWxF'

client = ZoomClient(API_KEY, API_SECRET)

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

for user in user_list['users']:
    user_id = user['id']
    print(json.loads(client.meeting.list(user_id=user_id).content))