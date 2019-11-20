# Necessary to import functions from different directory
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from sentiment_analysis import tweet_sentiment_classifier
from unittest import TestCase

class sentimentTests(TestCase):
    def test_postive(self):
         text = "I am happy about this product"
         reaction = tweet_sentiment_classifier(text)
         self.assertEqual(reaction, 1)

    def test_negative(self):
         text = "I hate this product"
         reaction = tweet_sentiment_classifier(text)
         self.assertEqual(reaction, -1)

    def test_neutral(self):
         text = "This product is red"
         reaction = tweet_sentiment_classifier(text)
         self.assertEqual(reaction, 0) 