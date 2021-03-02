import telebot
from telebot import types
import qrcode

token = '1600213684:AAFRxafQlwcZIQ7IJreXpRSW4t7Rsh5EHX4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    opened_sticker = open('static/sticker.webp','rb')
    bot.send_sticker(message.chat.id,opened_sticker)
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}  я бот для QRcode чтобы узнать всё /help')
    
@bot.message_handler(commands=['help'])
def aaa(message):
    bot.send_message(message.chat.id,f' все команды /start,/generate_qr_code')

@bot.message_handler(commands=['generate_qr_code'])
def generate(message):
    msg = bot.send_message(message.chat.id,'ввидете текст каторый нужен преврашать QRcode')
    bot.register_next_step_handler(msg,lala)

def lala(message):
    img = qrcode.make(message.text)
    saved_img = img.save('static/qr.png')
    open_id = open('static/qr.png','rb')
    bot.send_photo(message.chat.id,open_id)


bot.polling(none_stop=True)