import asyncio

from telebot.async_telebot import AsyncTeleBot
from telebot import types

from config import settings

token = settings.TELEGRAM_TOKEN
grouplist = ["9ПЗ4.21", "9ЗБ3.22", 'ПЗ3.20', 'ПЗ3.22']
bot_state = {
    "is_waiting_for_schedule": False
}
bot = AsyncTeleBot(token)



@bot.message_handler(commands=['start', 'help'])
async def start_message(message):
    await bot.reply_to(message, 'Hi 👾')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Добавить рвсписание!', callback_data='add_schedule'))
    await bot.send_message(message.chat.id, 'ヾ(•ω•`)o', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    if bot_state["is_waiting_for_schedule"]:
        bot_state["is_waiting_for_schedule"] = False
        await bot.reply_to(message, "вот такое расписание пользователь скинул: " + message.text) 


@bot.callback_query_handler(func=lambda callback: True)
async def callback_message(callback):
    if callback.data == 'add_schedule':
        await bot.send_message(callback.message.chat.id, 'Ну ты походу бивень .. 🐘')
        markup = types.InlineKeyboardMarkup()
        for g in grouplist:
            markup.add(types.InlineKeyboardButton(g, callback_data='get_schedule'))
        await bot.send_message(callback.message.chat.id, 'Выбери группу💩:', reply_markup=markup)
    elif callback.data == 'get_schedule':
        bot_state["is_waiting_for_schedule"] = True
        await bot.send_message(callback.message.chat.id, 'Напиши расписание:')


asyncio.run(bot.polling())
