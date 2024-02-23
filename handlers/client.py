import webbrowser
from aiogram import types, Dispatcher
from create_imports import bot
from aiogram import types
from keybords.button import kb_client
from database.SQL_db import get_all_products
from keybords.inline_buttons import inline_product_buy


async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Привіт {message.from_user.first_name} {message.from_user.last_name} тебе вітає бренд українського одягу Pijama Looks", reply_markup=kb_client())
    await message.delete()
    
@dispatcher_.message_handler(lambda message: "Shop" in message.text)
async def shop_button(message: types.Message):
    # Fetch products from the database using the get_all_products function
    products = await get_all_products()

    for product in products:
        product_id = product[0]
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=product[1],
            caption=f'Name: {product[2]}\nDescription: {product[2]}\nPrice: {product[4]}\n',
            reply_markup=inline_product_buy(product_id)  
        )

@dispatcher_.message_handler(lambda message: "Instagram" in message.text)
async def instagram_button(message: types.Message):
    webbrowser.open('https://www.instagram.com/pijama_looks/')
    await message.answer('Instagram')

def register_handler_client(dispatcher_: Dispatcher):
    dispatcher_.register_message_handler(start, commands=['start'])
