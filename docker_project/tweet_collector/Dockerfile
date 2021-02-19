# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Set the working directory to /app
COPY requirements.txt /app

# Copy the tweet collector script to /app
COPY get_tweets_streaming.py /app

# Copy the tweet collector script to /app
COPY config.py /app

# Edit the script to print tweets (use the logging module)

RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /app

CMD ["python", "get_tweets_streaming.py"]