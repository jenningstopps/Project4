FROM python

RUN apt-get update

COPY "C:\Users\jenni\CS446Assignment4\requirements.txt" /app

RUN pip install requirements.txt
