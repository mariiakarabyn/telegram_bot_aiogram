from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_imports import bot
from aiogram.dispatcher.filters import Text 
from database import SQL_db
from dotenv import load_dotenv, find_dotenv
from keybords import kb_client, inline_buttons
from keybords.admin_buttons import button_case_admin
from keybords.inline_buttons import action

import os 


load_dotenv(find_dotenv())
ID = (os.getenv('ADMIN_ID'))


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    
async def make_changes_comand(message: type.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(
        message.from_user.id,
        'Welcome! Please select action',
        reply_markup=button_case_admin(),
        parse_mode=None
    )


async def show_all_products(message: type.Message, products: list) -> None:
    if message.from_user.id == ID:
        for product in products:
            product_id = product[0]
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=product[1],
                                 caption=f"Name: {product[2]}\n Description: {product[3]}\nPrice: {product[4]}\n ",
                                 reply_markup=inline_buttons.inline_products_kb(product_id))
    else:
        await message.answer("You are not authorized to platform this action")
        

async def cb_all_products(message: type.Message):
    products = await SQL_db.get_all_products()
    
    if not products:
        await message.delete()
        await message.answer('We have no products')
        return
    
    await message.delete()
    await show_all_products(message, products)
    
    
async def cm_start(message: type.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Download Photo')
        

async def cancel_handler(message: type.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK. You have canceled the action!')
         

async def load_photo(message: type.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file.id
            await FSMAdmin.next()
            await message.reply('Enter the name of your product:')  
            
       
async def load_name(message: type.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Enter the description of your product:')  
            
            
async def load_description(message: type.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Enter the price of your product:') 

    
async def load_price(message: type.Message, state: FSMContext):
    if message.from_user.id == ID:
        try:
            price = float(message.text)
        except ValueError:
            error_message = "Invalide price value. Plese enter valid number "
            await message.reply(error_message)
            return
        
        async with state.proxy() as data:
            data['price'] = float(message.text)
            
        await SQL_db.sql_add_comand(state)
        await message.reply('Thank you! Your product has been created!')
        await state.finish()
        

async def admin_delete_product(callback: types.CallbackQuery, callback_data: dict):
    await SQL_db.delete_product(callback_data['id'])
    await callback.message.reply('Your product has been successefullly removed')
    
    
async def finish(message: types.Message):
    if message.from_user.id == ID:
        await message.reply('Finish!', reply_marcup=kb_client())
        await message.delete()
        

def register_handler_admin(dispatcher_: Dispatcher):
    dispatcher_.register_message_handler(cm_start, text=['Download'], state=None)
    dispatcher_.register_message_handler(cancel_handler, state=FSMAdmin.photo, text=['Cancel'])
    dispatcher_.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state='*')
    dispatcher_.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dispatcher_.register_message_handler(load_name, state=FSMAdmin.name)
    dispatcher_.register_message_handler(load_description, state=FSMAdmin.description)
    dispatcher_.register_message_handler(load_price, state=FSMAdmin.price)
    dispatcher_.register_message_handler(make_changes_comand, commands=['admin'], is_chat_admin=True)
    dispatcher_.register_message_handler(cb_all_products, text=['Products'])
    dispatcher_.register_message_handler(admin_delete_product, action.filter(action='Delete'))
    dispatcher_.register_message_handler(finish, text=['Finish'])







    
             
                     
