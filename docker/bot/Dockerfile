FROM python:3.7.8-slim-stretch

WORKDIR /root/weather_bot

ADD  .  ./

RUN pip install requests==2.24.0 \
    pytelegrambotapi==3.7.2 \
    python-dotenv==0.14.0 \
    emojiflags==0.1.1
RUN pip install flask

CMD python docker/bot/bot_implementation.py