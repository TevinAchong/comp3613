import tweepy

# Authorization using Twitter API
consumer_key = 'ENTER KEY HERE'
consumer_secret = 'ENTER KEY HERE'
access_token = 'ENTER KEY HERE'
access_token_secret = 'ENTER KEY HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Pulling tweets for a specific business
def pull_tweets(user_id, count, prt=False):
    tweets = api.user_timeline(
        '@' + user_id, count=count, tweet_mode='extended'
    )
    tw = []
    for t in tweets:
        tw.append(t.full_text)
        if prt:
            print(t.full_text)
            print()
    return tw
