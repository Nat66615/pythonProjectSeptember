import settings
from free_utils.keyboards_and_buttons import create_chat_keyboard
from telebot import TeleBot

bot = TeleBot(settings.SECRET_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Выберите стеллаж: ',
        reply_markup=create_chat_keyboard('Стеллаж', 5)
    )


@bot.callback_query_handler(func=lambda call: True)
def key_result(call):
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )


bot.polling(none_stop=True)
