from emojiflags.lookup import lookup
import telebot
import requests

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name} отпрваь нужный город или локацию'
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    url = f"http://127.0.0.1:8000/weather/lat={message.location.latitude}&lon={message.location.longitude}"
    resp = requests.get(url).json()
    final_message = f"Город: {resp['weathers']['location'][0]['city']}" \
                    f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                    f"Температура: {resp['weathers']['temperature']} "
    bot.send_message(message.chat.id, final_message)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    url = f"http://127.0.0.1:8000/weather/q={get_message_bot}"
    try:
        resp = requests.get(url).json()
        final_message = f"Город: {resp['weathers']['location'][0]['city']}" \
                        f"{lookup(resp['weathers']['location'][0]['country']['name'])}\n" \
                        f"Температура: {resp['weathers']['temperature']}"
        bot.send_message(message.chat.id, final_message)
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка\nПопробуйте еще раз')


bot.polling(none_stop=True)
