

import telebot
from telebot import types

bot = telebot.TeleBot('1761611912:AAHipgS9DZfrGfYFZyWOaltpT1qFXo_rHMM')

@bot.message_handler(commands=["start"])
def startKBoard(message):
    bot.send_message(message.chat.id, "Вы хотите знать расписание?(Да/Нет)")

@bot.message_handler(content_types=['text'])
def Nedelya(message):
    if message.text in ["Да", "ДА", "да", "дА", "Так", "Yes"]:
        catalogKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        Monday = types.KeyboardButton(text="Понедельник")
        Tuesday = types.KeyboardButton(text="Вторник")
        Wednesday = types.KeyboardButton(text="Среда")
        Thursday = types.KeyboardButton(text="Четверг")
        Friday = types.KeyboardButton(text="Пятница")
        catalogKBoard.add(Monday, Tuesday, Wednesday, Thursday, Friday)
        bot.send_message(message.chat.id, "Выберите день недели", reply_markup=catalogKBoard)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, "Работа закончена")
    elif message.text == "Понедельник":
        bot.send_message(message.chat.id, "1: Технологии защиты информации (лекция)")
        bot.send_message(message.chat.id, "2: Компьютерные сети (лекция)")
        bot.send_message(message.chat.id, "3: Технологии защиты (практика)")
    elif message.text == "Вторник":
        bot.send_message(message.chat.id, "1: Организация БД (практика)")
        bot.send_message(message.chat.id, "2: Организация БД (лекция)")
        bot.send_message(message.chat.id, "3: Многочисленные методы (лекция)")
        bot.send_message(message.chat.id, "4: Компьютерные сети (практика)")
        bot.send_message(message.chat.id, "5: Многочисленные методы (практика)")
    elif message.text == "Среда":
        bot.send_message(message.chat.id, "1: Окно/Инструментальные средства управления проектами (практика)")
        bot.send_message(message.chat.id, "2: Компьютерные сети (практика)")
        bot.send_message(message.chat.id, "3: Методы и технологии инженерии по (лекция)")
    elif message.text == "Четверг":
        bot.send_message(message.chat.id, "1: Мигалка Инструментальные средства управления проектами (лекция)/ нет пары")
        bot.send_message(message.chat.id, "2: Архитектура компьютеров (лекция)")
        bot.send_message(message.chat.id, "3: Архитектура компьютеров (практика)")
        bot.send_message(message.chat.id, "4: Методы и технологии инженерии по (практика)")
    elif message.text == "Пятница":
        bot.send_message(message.chat.id, "3: Межфакультетская дисциплина")
    else:
        bot.send_message(message.chat.id, "Попробуйте ответить ещё раз")
if __name__ == '__main__':
    bot.infinity_polling()

