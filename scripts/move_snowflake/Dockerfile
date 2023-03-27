FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY ./requirements.txt /usr/app
COPY ./load.py /usr/app
COPY ./helpers.py /usr/app
COPY ./config.py /usr/app
COPY ./config2.py /usr/app
COPY ./config_snow.py /usr/app

RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "./load.py" ]