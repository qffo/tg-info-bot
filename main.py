import telebot
import os
from telebot import types
from telebot import apihelper
from dotenv import load_dotenv

load_dotenv()


# PROXY_URL = "http://proxy.server:3128"

# bot = telebot(token=os.environ.get('TOKEN'), proxy=PROXY_URL)

TOKEN = os.getenv('TOKEN')
my_chat_id = os.getenv('MY_CHAT_ID')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Услуги')
    button2 = types.KeyboardButton(text='Сайт')
    button3 = types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button1, button2, button3)
    bot.send_message(
        message.chat.id, 'Привет! Я Виктор, и это мой бот ))) ! Добро пожаловать', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(
        text='Ссылка на сайт', url='https://ya.ru')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Информация', reply_markup=keyboard)


def send_request(message):
    mes = f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку.')


def send_service(message):
    bot.send_message(message.chat.id, '1. Помощь по функциям')
    bot.send_message(message.chat.id, '2. Разбор заданий')
    bot.send_message(message.chat.id, '3. Консультации')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'сайт':
        info_func(message)
    if message.text.lower() == 'оставить заявку':
        bot.send_message(
            message.chat.id, 'Напишите пожалуйста своё имя и номер телефона, что бы мы могли вам перезвонить.')
        bot.register_next_step_handler(message, send_request)
    if message.text.lower() == 'услуги':
        send_service(message)


apihelper.TIMEOUT = 60

# Что бы бот работал постоянно
bot.polling(none_stop=True)
