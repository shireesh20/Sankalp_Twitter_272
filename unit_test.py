"""
@Author: Mohith
@Purpose: This is used for unit testing which tests create tweet with valid and invalid data, delete tweet
"""

import unittest
from tweet import app

import string
import random


class TweetAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_tweet(self):
        N = 7
        res = ''.join(random.choices(string.ascii_lowercase +
                                     string.digits, k=N))

        response = self.app.post('/create_tweet', data={'tweetText': str(res)})
        if response.status_code == 302 or response.status_code == 200:
            print("Tweet creation successful.")
            print("Test case 1 successful")
        else:
            print("Tweet creation failed with status code:", response.status_code)
            print("Test case 2 failed")

        assert response.status_code == 302 or response.status_code == 200

    def test_create_tweet_invalid_data(self):
        response = self.app.post('/create_tweet', data={})
        if response.status_code == 500:
            print("Invalid tweet data. Bad request.")
            print("Test case 2 successful")
        else:
            print("Unexpected error with status code:", response.status_code)
            print("Test case 2 failed")

        self.assertEqual(response.status_code, 500)

    def test_delete_tweet(self):
        N = 7
        res = ''.join(random.choices(string.ascii_lowercase +
                                     string.digits, k=N))
        create_response = self.app.post('/create_tweet', data={'tweetText': str(res)})
        create_data = create_response.get_json()
        tweet_id_to_delete = create_data.get('id')  # Get the ID of the created tweet

        # Now, delete the created tweet
        delete_response = self.app.post(f'/delete_tweet/{tweet_id_to_delete}')

        if delete_response.status_code == 302:
            print("Tweet deletion successful.")
            print("Test case 3 successful")
        else:
            print("Tweet deletion failed with status code:", delete_response.status_code)
            print("Test case 3 failed")

        self.assertEqual(delete_response.status_code, 302) 

if __name__ == '__main__':
    unittest.main()
