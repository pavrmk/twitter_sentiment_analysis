import config
from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import pymongo

def authenticate():
    """Function for handling Twitter Authentication. 
       This script assumes you have a file called config.py
       which stores the 2 required authentication tokens:

       1. API_KEY
       2. API_SECRET
     
    """
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    return auth

if __name__ == '__main__':
    auth = authenticate()
    api = API(auth)

    cursor = Cursor(
        api.user_timeline,
        id = 'vonderleyen',
        tweet_mode = 'extended'
    )

    for status in cursor.items(100):
        tweet = {
            'text': status.full_text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count
        }
        print(tweet)

client = pymongo.MongoClient("mongodb")
db = client.tweets
collection = db.tweet_data