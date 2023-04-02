FROM python:3.9-slim-buster

WORKDIR /usr/app

RUN apt-get update && apt-get install -y wget

# Install Java
RUN apt-get install -y default-jre

# Download and extract Spark
RUN mkdir local && \
    wget -q https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz -O - | tar -xz -C /usr/app/local

# Set environment variables
ENV SPARK_HOME=/usr/app/local/spark-3.3.2-bin-hadoop3
ENV PATH=$PATH:$SPARK_HOME/bin

COPY ./requirements.txt /usr/app
COPY ./load.py /usr/app
COPY ./helpers.py /usr/app
COPY ./config.py /usr/app
COPY ./config2.py /usr/app
COPY ./config_snow.py /usr/app

RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "./load.py" ]