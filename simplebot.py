# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, '''Salom men aqlli botman.
    Sizlarga har xil qiziqarli savollar beraman.
    Tayyormisiz? /savol ga bosing
    ''')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, '''Bot quyidagi buyruqlardan iborat
    /start - Botga kirish
    /help - Yordam
    /savol - Savollar
    ''')

@bot.message_handler(commands=['savol'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, '''Dunyo mamlakatlari poytaxtlarini bilasizmi?
    1.O`zbekiston poytaxti''')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "toshkent":
        bot.send_message(message.chat.id, "Poytaxt nomlari katta harf bilan boshlanadi")
    elif message.text == "Toshkent":
            bot.send_message(message.chat.id, '''5 ochko to'pladingiz
    2.XXR poytaxti?''')
    elif message.text == "Pekin":
            bot.send_message(message.chat.id, '''10 ochko to'pladingiz
    Gretsiya poytaxti?''')
    elif message.text == "Afina":
            bot.send_message(message.chat.id, '''15 ochko to'pladingiz
     Germaniya poytaxti?''')
    elif message.text == "Berlin":
            bot.send_message(message.chat.id, '''20 ochko to'pladingiz
     Ukraina poytaxti?''')
    elif message.text == "Kiyev":
            bot.send_message(message.chat.id, '''25 ochko to'pladingiz
     Belarus poytaxti?''')
    elif message.text == "Minsk":
            bot.send_message(message.chat.id, '''30 ochko to'pladingiz
     Chexiya poytaxti?''')
    elif message.text == "Praga":
            bot.send_message(message.chat.id, '''35 ochko to'pladingiz
     Latviya poytaxti?''')
    elif message.text == "Riga":
            bot.send_message(message.chat.id, '''40 ochko to'pladingiz
     Estoniya poytaxti?''')
    elif message.text == "Tallin":
            bot.send_message(message.chat.id, '''45 ochko to'pladingiz
     Avstriya poytaxti?''')
    elif message.text == "Vena":
            bot.send_message(message.chat.id, '''50 ochko to'pladingiz
     Tailand poytaxti?''')
    elif message.text == "Bangkok":
            bot.send_message(message.chat.id, '''55 ochko to'pladingiz
     Bangladesh poytaxti?''')
    elif message.text == "Dakka":
            bot.send_message(message.chat.id, '''60 ochko to'pladingiz
     Qatar poytaxti?''')
    elif message.text == "Doha":
            bot.send_message(message.chat.id, '''65 ochko to'pladingiz
     Isroil poytaxti?''')
    elif message.text == "Quddus":
            bot.send_message(message.chat.id, '''70 ochko to'pladingiz
     Nepal poytaxti?''')
    elif message.text == "Katmandu":
            bot.send_message(message.chat.id, '''75 ochko to'pladingiz
     Filippin poytaxti?''')
    elif message.text == "Manila":
            bot.send_message(message.chat.id, '''80 ochko to'pladingiz
     Butan poytaxti?''')
    elif message.text == "Tximpxu":
            bot.send_message(message.chat.id, '''85 ochko to'pladingiz
     Nigeriya poytaxti?''')
    elif message.text == "Abudja":
            bot.send_message(message.chat.id, '''90 ochko to'pladingiz
     Somaliya poytaxti?''')
    elif message.text == "Mogadisho":
            bot.send_message(message.chat.id, '''95 ochko to'pladingiz
     Madagaskar poytaxti?''')
    elif message.text == "Antananarivu":
            bot.send_message(message.chat.id, 'Qoyile 100 ochko to`pladingiz')
    else:
        bot.send_message(message.chat.id, "Siz noto'g'ri javob berdingiz")

@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass


bot.polling(none_stop=True, interval=0)


