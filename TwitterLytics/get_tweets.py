#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy #as tw
import pandas #as pd

#Variables that contains the user credentials to access Twitter API 
consumer_key = 'aFsxpQHBxkqJ8y7KGG8n3Oqc3'
consumer_secret = 'srxxl0XJQ9jghAD69W5gyzHFCAZQn0y0AqXL0IUxqUDmtEw00t'
access_token ='1117216922091831296-y3hTZX1IoEUWFOo2G9TZIR69iO1G4p'
access_token_secret ='WwtrWyuOe4qzVre3vQKv2lKUq0O8ig12ZVwNbrK7sw68q'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def get_data(search, date, amount):

    search_wrd = search + "-filter:retweets"
    date_since = date

    #this pulls the amount of amount of tweets for the requested item
    tweets = tweepy.Cursor(api.search, 
                            q=search_wrd,
                            lang="en",
                            since_id=date_since).items(int(amount))

    #placing only the imporatant information into a table
    users_locs = [[c,tweet.user.id,tweet.user.screen_name, tweet.user.location,tweet.text] for c ,tweet in enumerate(tweets,1)]


    #place the users_loc into a dataframe so it can be transferred to a csv file
    tweet_text = pandas.DataFrame(data=users_locs, 
                        columns=['id','user_id','user', "location","text"])

    tweet_text.to_csv('data.csv',index=None)

    file_csv = open('data.csv', 'rb')
    contents = file_csv.readlines()
    #array = str(contents, 'utf-8').split(',')
    print(contents[0])
    array = str(contents[1], 'utf-8').split(',')
    print(array[4])

if __name__ == '__main__':
    get_data('Manchester United', '01-02-2019', 100)