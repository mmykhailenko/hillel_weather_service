from emojiflags.lookup import lookup
import telebot
import requests
import logging
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

weather_api_host = os.environ.get("WEATHER_API_HOST")


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name} отправь нужный город или локацию'
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    url = f"http://{weather_api_host}/weather/lat={message.location.latitude}&lon={message.location.longitude}"
    resp = requests.get(url).json()
    final_message = f"<b>Город:</b> {resp['weathers']['location'][0]['city']}" \
                    f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                    f"<b>Температура:</b> 🌡️ {resp['weathers']['temp_min']}°C...{resp['weathers']['temp_max']}°C\n"\
                    f"\n" \
                    f"<b>Сейчас:</b> {resp['weathers']['temperature']}°C\n" \
                    f"\n" \
                    f"<b>Давление:</b> {resp['weathers']['pressure']} HPA\n" \
                    f"<b>Влажность:</b> 💧 {resp['weathers']['humidity']}%\n" \
                    f"<b>Скорость ветра:</b> 💨 {resp['weathers']['wind_speed']} м/с\n" \
                    f"<b>Description:</b> 📄 {resp['weathers']['description']} \n"
    bot.send_message(message.chat.id, final_message, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    url = f"http://{weather_api_host}/weather/q={get_message_bot}"
    try:
        resp = requests.get(url).json()
        final_message = f"<b>Город:</b> {resp['weathers']['location'][0]['city']}" \
                        f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                        f"<b>Температура:</b> 🌡️ {resp['weathers']['temp_min']}°C...{resp['weathers']['temp_max']}°C\n"\
                        f"\n" \
                        f"<b>Сейчас:</b> {resp['weathers']['temperature']}°C\n" \
                        f"\n" \
                        f"<b>Давление:</b> {resp['weathers']['pressure']} HPA\n" \
                        f"<b>Влажность:</b> 💧 {resp['weathers']['humidity']}%\n" \
                        f"<b>Скорость ветра:</b> 💨 {resp['weathers']['wind_speed']} м/с\n" \
                        f"<b>Description:</b> 📄 {resp['weathers']['description']} \n"
        bot.send_message(message.chat.id, final_message, parse_mode='HTML')
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка!\nГород не найден!\nПопробуйте еще раз')
        logging.exception('')


bot.polling(none_stop=True)
