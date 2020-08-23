import os

from emojiflags.lookup import lookup
import telebot
import requests
from flask import Flask, request
import config
import logging

server = Flask(__name__)
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
WEATHER_API_HOST = config.weather_api_host


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name} отправь нужный город или локацию'
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    url = f"{WEATHER_API_HOST}/weather/lat={message.location.latitude}&lon={message.location.longitude}"
    resp = requests.get(url).json()
    final_message = f"Город: {resp['weathers']['location'][0]['city']}" \
                    f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                    f"Температура: {resp['weathers']['temperature']} "
    bot.send_message(message.chat.id, final_message)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    url = f"{WEATHER_API_HOST}/weather/q={get_message_bot}"
    try:
        resp = requests.get(url).json()
        final_message = f"Город: {resp['weathers']['location'][0]['city']}" \
                        f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                        f"Температура: {resp['weathers']['temperature']}"
        bot.send_message(message.chat.id, final_message)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка\nПопробуйте еще раз')
        logging.exception('')


@server.route('/' + config.TELEGRAM_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    url = f'https://hillel-weather-bot.herokuapp.com/{config.TELEGRAM_TOKEN}'
    print(url)
    bot.set_webhook(url=url)
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
