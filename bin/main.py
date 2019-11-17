# Necessary to import functions from different directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sentiment_analysis.sentiment_analysis import tweet_sentiment_classifier

if __name__ == '__main__':
    print(tweet_sentiment_classifier("Hated it"))