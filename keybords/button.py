from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def kb_client():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("Products", callback_data="Shop"),
        InlineKeyboardButton("Instagram", url="https://www.instagram.com/pijama_looks/"),
        # Add more buttons as needed
    ]
    return keyboard