from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Globally declaring the analyzer
analyser = SentimentIntensityAnalyzer()

def tweet_polarity_scores(tweet):
    '''
    Input: a tweet in the form of a string
    Output: polarity scores for that tweet indicating positive, negative, and neutral
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

if __name__ == '__main__':
    print(tweet_polarity_scores("This movie is VERY GOOD!"))
