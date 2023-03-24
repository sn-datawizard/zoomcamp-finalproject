FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY ./requirements.txt /usr/app
COPY ./upload_mongodb.py /usr/app
COPY ../helpers.py /usr/app
COPY ../config.py /usr/app

RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "./upload_mongodb.py" ]