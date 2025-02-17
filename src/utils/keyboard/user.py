from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)

# example for your InlinekeyboardMarkup(that means, inside text)
# for example ReplyKeyboardMarkup you can see inside admin.py(src.utils.keyboard.admin)

master_panel_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='🗓 Управление расписанием', callback_data='schedule_management')],

        [
        InlineKeyboardButton(text='👥 Клиенты', callback_data='clients'),
        InlineKeyboardButton(text='📝 Записи', callback_data='records'),
        ],

        [
        InlineKeyboardButton(text='📅 Сегодня', callback_data='today'),
        InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings'),
        ],
    ]
)