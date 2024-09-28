from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('7943747641:AAEtG31aBbxjaMvCPKbGZmPbSrwvf-daqwA')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть приложение', web_app=WebAppInfo(url='')))
    await message.answer('Привет,студент!', reply_markup=markup)
executor.start_polling(dp)

