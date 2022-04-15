from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN

# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин, {message.from_user.full_name}!")

# @dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup1 = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )

    markup1.add(button_call_1)
    question = "Какой язык программирования по вашему мнению самый простой?"
    answers = ['Java', 'C++', 'Unity', 'Python']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3,
                        reply_markup=markup1
                        )


# @dp.message_handler(commands=['quiz1'])
async def quiz1(message: types.Message):
    markup2 = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_2"
    )
    markup2.add(button_call_2)

    question = "Какая страна производит больше всего кофе в мире?"
    answers = 'Колумбия Индонезия Бразилия Вьетнам'.split()
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup2
                        )

# @dp.message_handler(commands=["ban"], commands_prefix="!/")
async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id != ADMIN:
            await message.reply("Ты не мой БОСС!")

        if not message.reply_to_message:
            await message.reply("Команда должна быть ответом на сообщение!")

        else:
            await message.bot.delete_message(message.chat.id, message.message_id)
            await message.bot.kick_chat_member(message.chat.id, user_id=message.reply_to_message.from_user.id)
            await bot.send_message(
                message.chat.id,
                f"{message.reply_to_message.from_user.full_name} забанен по воле администратора {message.from_user.full_name}")

    else:
        await message.answer("Данная команда доступна только в группах!")

def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=["start"])
    dp.register_message_handler(quiz, commands=["quiz"])
    dp.register_message_handler(quiz, commands=["quiz1"])
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")