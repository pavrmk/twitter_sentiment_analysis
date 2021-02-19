import config
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import pymongo

TRACKING_KEYWORDS = 'artifical intelligence'

client = pymongo.MongoClient("mongodb")
db = client.tweets
collection = db.tweet_data

def authenticate():
    """Function for handling Twitter Authentication. 
       This script assumes you have a file called config.py
       which stores the 4 required authentication tokens:

       1. API_KEY
       2. API_SECRET
       3. ACCESS_TOKEN
       4. ACCESS_TOKEN_SECRET

    """
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    return auth

class MaxTweetsListener(StreamListener):

    def __init__(self, max_tweets, *args, **kwargs):
        # initialize the StreamListener
        super().__init__(*args, **kwargs)
        # set the instance attributes
        self.max_tweets = max_tweets
        self.counter = 0
        
    def on_connect(self):
        print('connected. listening for incoming tweets')

    def on_status(self, status):
        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""
        
        # increase the counter
        self.counter += 1        

        tweet = {
            'text': status.text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count
        }

        # store tweets
        collection.insert_one(tweet)

        # print the tweet
        print(f'New tweet arrived: {tweet["text"]}')

        # check if we have enough tweets collected
        if self.max_tweets == self.counter:
            # reset the counter
            self.counter=0
            # return False to stop the listener
            return False

    def on_error(self, status):
        if status == 420:
            print(f'Rate limit applies. Stop the stream.')
            return False

if __name__ == '__main__':
    auth = authenticate()
    listener = MaxTweetsListener(max_tweets=100)
    stream = Stream(auth, listener)
    stream.filter(track=[TRACKING_KEYWORDS], languages=['en'], is_async=False)