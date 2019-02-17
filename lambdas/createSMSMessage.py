import json

def lambda_handler(event, context):
    user = event['body']['user']['screen_name']
    id_str = event['body']['id_str']
    url = "https://twitter.com/" + user + "/status/" + id_str
    message = "Here's an neet tweet: " + url
    return message
