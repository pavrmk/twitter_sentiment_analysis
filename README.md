# Dockerized Data Pipeline that analyzes the sentiment of tweets

This project was created during the [@spicedacademy](https://github.com/spicedacademy/) boot camp. The goal of this project is to develop a dockerized data pipeline with following steps:
* Collecting tweets with a Python script
* Storing tweets in a MongoDB database
* ETL Job: Extracting the tweets from MongoDB, performing a sentiment analysis of the tweets and stroing the results in a second database (Postgres)
* Loading the tweets and the tweets sentiment in a Postgres database

<img src= "https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/structure.svg" width="830">

The pipeline should look like this in the Docker Desktop:

<img src= "https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/docker_pipeline.png" width="830">

This is what the Postgres DB with the tweets and corresponding sentiment score could look like:

<img src= "https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/postgres_tweets.png" width="830">

## To do:
* Finish the Slack bot and add it to the project description
