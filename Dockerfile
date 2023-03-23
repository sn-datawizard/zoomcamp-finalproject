FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY ./requirements.txt /usr/app
COPY ./scripts/test.py /usr/app
COPY ./scripts/helpers.py /usr/app
COPY ./scripts/config.py /usr/app

RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "./test.py" ]