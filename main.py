from flask import Flask
import telebot
import threading

API_TOKEN = '7732255219:AAGiKGARxcqPIIL95UWG56cwRa9eBm-1i94'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Farid Memory Bot работает 🧠'

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f'Принял: {message.text}')

def run_bot():
    bot.polling(non_stop=True)

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=8080)
