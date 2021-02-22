import pymongo
import time
from sqlalchemy import create_engine

time.sleep(10)  # Time (in seconds) to give Mongo a few seconds to start

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use within the MongoDB server
db = client.tweets

# Select the collection of documents you want to use within the MongoDB database
collection = db.tweet_data

# Establishing a Postgres DB connection: 
pg = create_engine('postgres://pavel:tweet123@postgresdb:5432/tweets_postgres_db', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

# Read a few entries from MongoDB, print them, and add them to the Postgres databse
entries = collection.find()
for e in entries:
    print(e)
    text = e['text']
    score = 1.0  # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))
