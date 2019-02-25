"""Lambda handler for polling twitter API with configured search."""

import twitter_proxy

def handler(event, context):
    print("Starting Poller")
    batch = _search_batches(event['searchText'])

    return {
        'statusCode': 200,
        'body': batch[0]
    }

def _search_batches(searchText):
    tweets = []
    while True:
        result = twitter_proxy.search(searchText)
        if not result['statuses']:
            # no more results
            break

        tweets = result['statuses']

        return tweets[0:1]
