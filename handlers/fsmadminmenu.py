from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def fsm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await bot.send_message(message.chat.id,
                           f"Салам хозяин, {message.from_user.full_name}! Пришлите фото блюда")

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, 'Название блюдо?')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, 'Добавьте описание:')

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await bot.send_message(message.chat.id, "Укажите цену:")


async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)
        await state.finish()
        await bot.send_message(message.chat.id, "Закончили")
    except:
        await bot.send_message(message.chat.id, "Отправлять только числа!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await message.reply("ОК")
        await state.finish()

def register_hendler_fsmAdminGetUser(dp: Dispatcher):
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_reg, state="*", commands="cancel")
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=["register"])
