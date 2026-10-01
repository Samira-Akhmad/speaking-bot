import telebot
TOKEN = "8957221106:AAF4_AyHYgxt_Orw9PMx4OUHqKx4GBjlRR0"
bot = telebot.TeleBot(TOKEN)
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/questions")
    markup.add(item1)
    bot.send_message(message.chat.id, "Hello! I am your bot. How can I help you today?", reply_markup=markup)

@bot.message_handler(commands=['questions'])
def questions(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Part 1")
    item2 = types.KeyboardButton("Part 2")
    item3 = types.KeyboardButton("Part 3")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Which part questions do you need?", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_questions(message):
    if message.text == "Part 1":
        bot.send_message(message.chat.id, "Here are part1 questions:\n" "1. What is your name?\n" "2. How old are you?\n"
              "3. Where do you live?\n" "4. What is your favorite color?\n" "5. What is your favorite food?\n", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Part 2":
        bot.send_message(message.chat.id, "Here are part2 questions:\n" "1. What is your favorite hobby?\n" "2. What is your favorite movie?\n"
              "3. What is your favorite book?\n" "4. What is your favorite sport?\n" "5. What is your favorite music genre?\n", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Part 3":
        bot.send_message(message.chat.id, "Here are part3 questions:\n" "1. What is your dream job?\n" "2. What is your biggest fear?\n"
              "3. What is your proudest achievement?\n" "4. What is your favorite travel destination?\n" "5. What is your favorite quote?\n", reply_markup=types.ReplyKeyboardRemove())
bot.infinity_polling()