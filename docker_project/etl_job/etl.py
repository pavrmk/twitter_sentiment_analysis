import pymongo
import time
from sqlalchemy import create_engine

time.sleep(10)  # seconds

# Establishing a Postgres DB connection: 
pg = create_engine('postgres://pavel:tweet123@host:5432/tweets_postgres_db', echo=True)

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use within the MongoDB server
db = client.tweets

# Select the collection of documents you want to use within the MongoDB database
collection = db.tweet_data

# Read a few entries from MongoDB and print them
entries = collection.find(limit=5)
for e in entries:
    print(e)