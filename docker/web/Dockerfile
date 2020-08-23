FROM python:3.6.11-slim-stretch

ENV PORT=8000

WORKDIR /root/weather_web

ADD weather /root/weather_web/weather
ADD weather_api /root/weather_web/weather_api
ADD utils /root/weather_web/utils
ADD manage.py requirements.txt wait-for-it.sh  ./

RUN chmod +x wait-for-it.sh && \
    pip install -r requirements.txt

CMD gunicorn weather_api.wsgi --bind 0.0.0.0:$PORT
