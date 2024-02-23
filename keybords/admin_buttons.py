from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def button_case_admin() -> ReplyKeyboardMarkup:
    admin_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_buttons.add(KeyboardButton(text='Download'),
                      KeyboardButton(text='Products'))
    
    admin_buttons.add(KeyboardButton(text='Cancel'),
                      KeyboardButton(text='Finish'))
    
    return admin_buttons
