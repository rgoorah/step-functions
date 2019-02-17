"""Twitter API Helper."""

import twitter

CONSUMER_KEY = '' # These will be revoked after the demo
CONSUMER_SECRET_KEY = ''# These will be revoked after the demo
ACCESS_TOKEN = '' # These will be revoked after the demo
ACCESS_TOKEN_SECRET = ''# These will be revoked after the demo

def search(search_text, since_id=None):
    """Search for tweets matching the given search text."""
    return TWITTER.GetSearch(term=search_text, count=100, return_json=True)


def _create_twitter_api():
    return twitter.Api(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET_KEY,
        access_token_key=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        tweet_mode='extended'
    )


TWITTER = _create_twitter_api()
