from aiogram import types, Dispatcher
from config import bot, dp


# @dp.message_handler()
async def echo_message(message: types.Message):

    bad_words = "java bitch дурак балбес эшек".split()
    for i in bad_words:
        if i in message.text.lower():
            await message.delete()
            await bot.send_message(message.chat.id,
                           f"{message.from_user.full_name}, сам ты {i}!!! не выражайся!"
                           )

    if message.text.lower() == 'dice':
        await bot.send_dice(message.chat.id, emoji="🎯")

def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)