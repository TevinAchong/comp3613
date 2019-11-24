'''
import json
import sys
import os
from unittest import TestCase

from get_tweets import retrieve_tweets_store_in_json
import datetime

class captureTest(TestCase):

    def test_JSONIsCreated(self):
        search = 'Google'
        Date = datetime.datetime(2019, 11, 20)
        amount = 1
        jsonFile = 'testFile.json'
        retrieve_tweets_store_in_json(search, Date, amount, jsonFile)
        self.assertTrue(os.path.exists('testFile.json'))
        #delete file after 
        os.remove('testFile.json')


'''
