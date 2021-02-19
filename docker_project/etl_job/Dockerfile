FROM python:3.8

# Set the working directory to /app
WORKDIR /etl

# Set the working directory to /app
COPY requirements.txt /etl

RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /etl

CMD ["python", "etl.py"]