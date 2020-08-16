import telebot
import requests
import config
import logging

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
weather_api_host = config.weather_api_host
weather_api_port = config.weather_api_port


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name} отправь нужный город или локацию'
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    url = f"http://{weather_api_host}:{weather_api_port}/weather/lat={message.location.latitude}&lon={message.location.longitude}"
    resp = requests.get(url).json()
    final_message = f"Город: {resp['weathers']['location'][0]['city']}\nТемпература: {resp['weathers']['temperature']}"
    bot.send_message(message.chat.id, final_message)

    bot.send_photo(message.chat.id, f'{resp["weathers"]["location"][0]["country"]["flag"]}')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    url = f"http://{weather_api_host}:{weather_api_port}/weather/q={get_message_bot}"
    try:
        resp = requests.get(url).json()
        final_message = f"Город: {resp['weathers']['location'][0]['city']}\nТемпература: {resp['weathers']['temperature']}"
        bot.send_message(message.chat.id, final_message)
        bot.send_photo(message.chat.id, f'{resp["weathers"]["location"][0]["country"]["flag"]}')
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка\nПопробуйте еще раз')
        logging.exception('')


bot.polling(none_stop=True)
