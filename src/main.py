import asyncio

from telebot.async_telebot import AsyncTeleBot
from telebot import types

from config import settings

token = settings.TELEGRAM_TOKEN
admin = settings.ADMIN_CHAT_ID
groups = {
    "9ПЗ4.21": -4875808929, 
    "9ЗБ3.22": -4798064565, 
    "ПЗ3.20": -5007386200, 
}
bot_state = {
    "group_name": "",
    "is_waiting_for_schedule": False
}
bot = AsyncTeleBot(token)


@bot.message_handler(commands=['start','Start'])
async def start_message(message):
    print("attempt to start: " + str(message.chat.id))
    if str(admin) == str(message.chat.id):
        await bot.reply_to(message, 'Привет')
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Добавить рвсписание!', callback_data='add_schedule'))
        await bot.send_message(message.chat.id, 'ヾ(•ω•`)o', reply_markup=markup)


@bot.message_handler(commands=['help'])
async def start_message(message):
    print("attempt to start: " + str(message.chat.id))
    await bot.reply_to(message, 'Привет, вот ващ тех.спец, иди к нему')
    markup = types.InlineKeyboardMarkup()
    #markup.add(types.InlineKeyboardButton('вот ващ тех.спец, иди к нему', callback_data='add_schedule'))
    await bot.send_message(message.chat.id, '@Vadik6388', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    print(message, message.chat.id)
    if str(admin) == str(message.chat.id):
        await bot.send_message(message.chat.id, 'ヾ(•ω•`)o')
        if bot_state["is_waiting_for_schedule"]:
            bot_state["is_waiting_for_schedule"] = False
            await bot.reply_to(message, "вот такое расписание пользователь скинул: " + message.text) 
            group_name2 = bot_state["group_name"]
            await bot.send_message(groups[group_name2], message.text)


@bot.callback_query_handler(func=lambda callback: True)
async def callback_message(callback):
    if str(admin) == str(callback.message.chat.id):
        if callback.data == 'add_schedule':
            await bot.send_message(callback.message.chat.id, 'Ну ты походу бивень .. 🐘')
            markup = types.InlineKeyboardMarkup()
            for g in groups.keys():
                markup.add(types.InlineKeyboardButton(g, callback_data='get_schedule_'+ str(g)))
            await bot.send_message(callback.message.chat.id, 'Выберите группу:', reply_markup=markup)
        elif 'get_schedule' in callback.data:
            bot_state["is_waiting_for_schedule"] = True
            bot_state["group_name"] = callback.data.replace("get_schedule_", "")
            await bot.send_message(callback.message.chat.id, 'Напишите расписание:')


asyncio.run(bot.polling())
