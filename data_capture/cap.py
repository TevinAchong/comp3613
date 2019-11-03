
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob("In 1992 Delta Air Lines had its", analyzer=NaiveBayesAnalyzer())
print(blob.sentiment)


# Retrieving all tweets mentioning <company_name>