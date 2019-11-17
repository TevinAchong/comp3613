from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

# Globally declaring the analyzer
analyser = SentimentIntensityAnalyzer()

def tweet_polarity_scores(tweet):
    '''
    Input: a tweet in the form of a string
    Output: polarity scores for that tweet indicating positive, negative, and neutral
        1 => Positive Tweet
        0 => Neutral Tweet
        -1 => Negative Tweet
    '''
    score = analyser.polarity_scores(tweet)
    compound = score['compound']
    
    # The tweet is considered positive
    if compound >= 0.05:
        return 1
    
    # The tweet is considered neutral
    elif (compound > -0.05) and (compound < 0.05):
        return 0
    
    # The tweet is considered negative
    else:
        return -1
