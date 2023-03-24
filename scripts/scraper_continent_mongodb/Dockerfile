FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY ./requirements.txt /usr/app
COPY ./scraper.py /usr/app
COPY ./helpers.py /usr/app
COPY ./config2.py /usr/app

RUN pip install --no-cache-dir -r ./requirements.txt

CMD [ "python", "./scraper.py" ]