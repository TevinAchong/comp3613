# Necessary to import functions from different directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sentiment_analysis.sentiment_analysis import tweet_sentiment_classifier
from tweet_capture.get_tweets import retrieve_tweets_store_in_json
import json
import argparse


def main(args_in):
    # Command line arguments
    parser = argparse.ArgumentParser(usage="tweet puller and sentiment analysis [options]")

    parser.add_argument("--company-name", dest="company_name", default="United Airlines",
                        help="Name of the company to search twitter for", required=True)
    parser.add_argument("--num-tweets", dest="num_tweets", default=200,
                        help="The amount of tweets to capture from twitter")
    parser.add_argument("--tweet-storage-file", dest="tweet_storage_file", default="../data/tweets.txt",
                        help="The path to the file which will hold the retrieved tweets")
    parser.add_argument("--search-date-since", dest="search_date_since", required=True,
                        help="Pull tweets since this date")
    parser.add_argument("--analysis-storage-file", dest="analysis_storage_file", default="../data/results.json",
                        help="The path to the file which will hold the results of the analyses")

    try:
        options = parser.parse_args(args_in)
    except argparse.ArgumentError:
        parser.print_help(sys.stderr)
        return -1
    
    # Perform the twitter query and store in json format
    retrieve_tweets_store_in_json(
        options.company_name,
        options.search_date_since,
        options.num_tweets,
        options.tweet_storage_file
    )

    # Getting the classifications for each tweet
    results = []
    sentiments = []
    texts = []
    locations = []
    with open(options.tweet_storage_file) as tweets_json:
        tweets = json.load(tweets_json)
        for tweet in tweets:
            tweet['sentiment_score'] = tweet_sentiment_classifier(tweet['full_text'])
            results.append(tweet)
            sentiments.append(tweet['sentiment_score'])
            texts.append(tweet['full_text'])
            locations.append(tweet['user']['location']) 
            
    # Storing the tweets and their sentiments in a file
    with open(options.analysis_storage_file, 'w') as analysis_file:
        json.dump(results, analysis_file)
    
    print(str(sentiments) + "|||" + str(texts)+ "|||" + str(locations))
    


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))