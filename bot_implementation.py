import telebot
import requests

bot = telebot.TeleBot('1385063094:AAEmWmMJXP54Oc-dsOBXFF7sdVw4e-lu1Kc')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет {message.from_user.first_name} отпрваь нужный город или локацию'
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    url = f"http://127.0.0.1:8000/weather/lat={message.location.latitude}&lon={message.location.longitude}"
    resp = requests.get(url).json()
    final_message = f"Город: {resp['weathers'][0]['city']}\nТемпература: {resp['weathers'][0]['temperature']}"
    bot.send_message(message.chat.id, final_message)

    bot.send_photo(message.chat.id, f'{resp["weathers"][0]["flag"]}')


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    url = f"http://127.0.0.1:8000/weather/q={get_message_bot}"
    try:
        resp = requests.get(url).json()
        final_message = f"Город: {resp['weathers'][0]['city']}\nТемпература: {resp['weathers'][0]['temperature']}"
        bot.send_message(message.chat.id, final_message)
        bot.send_photo(message.chat.id, f'{resp["weathers"][0]["flag"]}')
    except Exception:
        bot.send_message(message.chat.id, 'Ошибка\nПопробуйте еще раз')



bot.polling(none_stop=True)
