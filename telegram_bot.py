$ heroku create myapp --buildpack heroku/python


from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot('5439262260:AAGJlUpowvuwb-59McWxj-62a7jaMjtgCGA')
dp = Dispatcher(bot)
button1 = InlineKeyboardButton(text='новость', callback_data='post')
button2 = InlineKeyboardButton(text='вопрос', callback_data='issue')
button3 = InlineKeyboardButton(text='назад', callback_data='back')
button4 = InlineKeyboardButton(text='помощь', callback_data='help')
keyboard2 = InlineKeyboardMarkup(inline_keyboard=True).add(button3, button4)
keyboard = InlineKeyboardMarkup(inline_keyboard=True).add(button1, button2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply(text='Привет!\n'
                             'Я 0.5v HSE MATH bot.\n'
                             'Я умею пересылать сообщения @malaw',
                        reply_markup=keyboard)


@dp.message_handler(commands=['help', 'back'])
async def menu(message):
    await message.reply(text='Я 0.5v HSE MATH bot.\n'
                             'Я умею пересылать сообщения @malaw',
                        reply_markup=keyboard)


@dp.message_handler(commands=['issue', 'post'])
async def menu(message):
    await message.reply(text='Твоё следующее сообщение будет обработано как вопрос или пост\n'
                             'Для отмены действия нажми "назад"',
                        reply_markup=keyboard2)


@dp.message_handler(content_types=["audio", "text", "document", "photo"])
async def forward_image(message):
    if message.chat.id != 252406114:
        await bot.forward_message(252406114,
                                  message.chat.id,
                                  disable_notification=True,
                                  message_id=message.message_id)
        await bot.send_message(message.chat.id, text='Отправил')


@dp.callback_query_handler(text=['post', 'issue', 'back', 'help'])
async def answer(call: types.CallbackQuery):
    if call.data == 'post':
        await call.message.reply(text="Отправь мне пост",
                                 reply_markup=keyboard2)
    elif call.data == 'issue':
        await call.message.reply(text="Следующее сообщение будет "
                                      "отформатировано и отправлено в канал",
                                 reply_markup=keyboard2)
    elif call.data == 'back' or call.data == 'help':
        await call.message.reply(text='Я 0.5v HSE MATH bot.\n'
                                      'Я умею пересылать сообщения @malaw',
                                 reply_markup=keyboard)
    await call.answer()


@dp.message_handler(content_types=["text"])
async def make_post(message, contex=False):
    if contex:
        contex = False
        await bot.send_message(252406114,
                               disable_notification=True,
                               text="#issue\n" + message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
