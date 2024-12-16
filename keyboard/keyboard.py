from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

main_menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Каталог🛍️',
                                                                   callback_data='catalog')],
                                             [InlineKeyboardButton(text='Корзина🛒',
                                                                   callback_data='basket')],
                                             [InlineKeyboardButton(text='О насℹ️',
                                                                   callback_data='about_us')],
                                             [InlineKeyboardButton(text='Регистрация✅',
                                                                   callback_data='registration')]])

categories = {
    "category_running": {
        "menu_text": "Кроссовки для спорта",
        "id": 1
    },
    "category_casual" : {
        "menu_text": "Повседневные кроссовки",
        "id": 2
    },
    "category_kids": {
        "menu_text": "Детские кроссовки",
        "id": 3
    }
}
category_buttons = []
for category in categories:
    category_buttons.append([InlineKeyboardButton(text=categories[category]["menu_text"], callback_data=category)])
category_keyboard_inline = InlineKeyboardMarkup(inline_keyboard=category_buttons)