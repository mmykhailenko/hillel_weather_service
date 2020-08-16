FROM python:3.6.11-slim-stretch

WORKDIR /root/weather_web

ADD . ./

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000