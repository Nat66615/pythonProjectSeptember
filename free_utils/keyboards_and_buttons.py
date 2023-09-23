from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_chat_keyboard(title, buttons_quantity):
    return InlineKeyboardMarkup(row_width=3).add(
        *[
            InlineKeyboardButton(
                f' {title} {key_number}',
                callback_data=key_number
            ) for key_number in range(1, buttons_quantity + 1)
        ]
    )


def clear_chat_keyboard():
    pass
