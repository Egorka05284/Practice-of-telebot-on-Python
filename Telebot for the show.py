import telebot
from telebot import types


num_of_bot = 'TOKEN'
bot = telebot.TeleBot(num_of_bot)


@bot.message_handler(commands=["stop"])
def stop_bot(message):
    if message.text == "/stop":
        bot.send_message(message.chat.id, "Stopping...")
        bot.stop_bot()


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Go to the site", url='https://www.youtube.com')
    btn2 = types.InlineKeyboardButton("Delete a photo", callback_data='delete')
    btn3 = types.InlineKeyboardButton("Edit", callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    answer_on_photo = "I'm a bot I can't look photos I'm not an AI"
    bot.reply_to(message, answer_on_photo, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text("The text is edited", callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=["start"])
def text(message):
    mess = f"<b><em>Hi,  {message.from_user.first_name} {message.from_user.last_name}, I'm Egorka28_bot, I can give you" \
           f" 3 links on interesting videos and songs, just look the buttons below your screen and touch them</em></b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def button(message):
    Answer1 = 'https://www.youtube.com/watch?v=8e4ZRAE0ibk'
    Answer2 = 'https://www.youtube.com/watch?v=11dGxhtK-pA'
    Answer3 = 'https://www.youtube.com/watch?v=-ToHWV1uOTc&t=2302s'
    Answer4 = "Here are the buttons"
    mess = f"<b><em>Hi,  {message.from_user.first_name} {message.from_user.last_name}, I'm Egorka28_bot, I can give you" \
           f" 3 links on interesting videos and songs, just look the buttons below your screen and touch them</em></b>"
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Knopka = types.KeyboardButton("The buttons")
    WhoCreatedYou = types.KeyboardButton("Giving up the gun")
    NotGonnaGetUs = types.KeyboardButton("Not gonna get us")
    FemaleVoice = types.KeyboardButton("Female voices from WOT")
    markup2.add(WhoCreatedYou, NotGonnaGetUs, FemaleVoice, Knopka)


    if message.text == 'Giving up the gun':
        bot.send_message(message.chat.id, Answer1, reply_markup=markup2)
    elif message.text == 'Not gonna get us':
        bot.send_message(message.chat.id, Answer2, reply_markup=markup2)
    elif message.text == 'Female voices from WOT':
        bot.send_message(message.chat.id, Answer3, reply_markup=markup2)
    elif message.text == 'The buttons':
        bot.send_message(message.chat.id, Answer4, reply_markup=markup2)
    elif message.text.lower() == 'hello':
        bot.send_message(message.chat.id, mess, parse_mode='html')
    else:
        bot.reply_to(message, "I didn't get it you please use the buttons or write me ""Hello""")
bot.polling(none_stop=True)
