#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas
import json

#Variables that contain the user credentials to access Twitter API 
consumer_key = 'aFsxpQHBxkqJ8y7KGG8n3Oqc3'
consumer_secret = 'srxxl0XJQ9jghAD69W5gyzHFCAZQn0y0AqXL0IUxqUDmtEw00t'
access_token ='1117216922091831296-y3hTZX1IoEUWFOo2G9TZIR69iO1G4p'
access_token_secret ='WwtrWyuOe4qzVre3vQKv2lKUq0O8ig12ZVwNbrK7sw68q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_tweets_store_in_json(search, date, amount, json_file):
    search_wrd = search + "-filter:retweets"
    date_since = date

    #this pulls the amount of amount of tweets for the requested item
    tweets = tweepy.Cursor(api.search, 
                            q=search_wrd,
                            lang="en",
                            since_id=date_since,
                            tweet_mode='extended').items(int(amount))

    # Dump all the tweets into JSON format
    tweets_arr = []
    for t in tweets:
        tweets_arr.append(t._json)
    with open(json_file, 'w') as outfile:
        json.dump(tweets_arr, outfile)
    