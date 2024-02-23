from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import Dispatcher

# Define your CallbackData object
action = types.CallbackData("action", "in", "action")

def inline_products_kb(product_id: int) -> types.InlineKeyboardMarkup:
    product_kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Delete', callback_data=action.new(id=product_id, action='Delete'))]
    ])
    return product_kb

def inline_product_buy(product_id: int) -> types.InlineKeyboardMarkup:
    product_kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Buy', callback_data=action.new(id=product_id, action='Buy'))]
    ])
    return product_kb
