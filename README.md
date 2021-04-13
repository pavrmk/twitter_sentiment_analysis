# Dockerized Data Pipeline that analyzes the sentiment of tweets

This project was created during the [@spicedacademy](https://github.com/spicedacademy/) boot camp. The goal of this project is to develop a dockerized data pipeline with following steps:

<kbd>
  <h4>① Collecting tweets with a Python script</h4>
  <h4>② Storing tweets in a MongoDB database</h4>
  <h4>③ ETL Job: Extracting the tweets from MongoDB, performing a sentiment analysis of the tweets and stroing the results in a Postgres database</h4>
  <h4>④ Loading the tweets and the tweets sentiment in a Postgres database</h4>

  <img src="https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/structure-gray.png">
</kbd>
<br>
<br>

The pipeline should look like this in the Docker Desktop:

<kbd>
  <img src="https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/docker_pipeline.png">
</kbd>
<br>
<br>

This is what the Postgres DB with the tweets and corresponding sentiment score could look like:

<kbd>
  <img src="https://github.com/pavrmk/twitter_sentiment_analysis/blob/main/images/readme_file_images/postgres_tweets.png">
</kbd>

## To do:
* Finish the Slack bot and add it to the project description
