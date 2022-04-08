# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:23:48 2021

@author: Javlonbek
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '1789620437:AAHiG55DBESVZS399V-RT8GKeo1TUvK-nro'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalamu alaykum!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
bot.polling()
