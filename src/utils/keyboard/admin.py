from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# example for your ReplyKeyboardMarkup (that means, inside panel for entering messages and other things),
# for example inside user.py you can see chat message (src.utils.keyboard.user)

admin_panel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Посмотреть приветственное сообщение')],
        [KeyboardButton(text='Отредактировать приветственное сообщение')]
    ],
    resize_keyboard=True
)

