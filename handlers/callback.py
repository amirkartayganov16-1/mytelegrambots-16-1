from aiogram import types, Dispatcher
from config import bot, dp

# @dp.callback_query_handler(lambda func: func.data == "button_call_1")
async def quiz1(call: types.CallbackQuery):
    question = "Какая страна производит больше всего кофе в мире?"
    answers = 'Колумбия Индонезия Бразилия Вьетнам'.split()
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2
                        )

# @dp.callback_query_handler(lambda func: func.data == "button_call_2")
async def quiz3(call: types.CallbackQuery):

    question = "Какой герой мультфильма живёт под водой?"
    answers = ['Рик', 'Гамбала', 'Губкабоб', 'Гэри']
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=5
                        )

def register_hendlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        quiz1,
        lambda func: func.data == "button_call_1"
    )

    dp.register_callback_query_handler(
        quiz3,
        lambda func: func.data == "button_call_2"
    )
