from create_imports import Bot, Dispatcher
from aiogram.types import Message, PreCheckoutQuery, ContentType
from aiogram import types
import os
from database.SQL_db import get_product_price, get_product_title, get_product_description
from keybords.inline_buttons import action

async def handle_buy_callback(callback: types.CallbackQuery, callback_data: dict):
    action_type = callback_data['action']
    product_id = callback_data['id']
    
    if action_type == 'Buy':
        title_ = await get_product_title(product_id)
        description_ = await get_product_description(product_id)
        price_ = await get_product_price(product_id)
        
        title_str = title_[0] if isinstance(title_, tuple) else str(title_)
        
        await bot.send_invoice(
            callback.from_user.id,
            title=title_str,
            description= description_,
            payload=str(product_id),
            provider_token=os.environ.get('PROVIDER_TOKEN'),
            start_parameter='payment',
            currency='UAH',
            prices=[types.LabeledPrice(label=title_str, amount=int(float(price_)*100))],
            need_name=True,
            need_phone_number=True,
            need_email=True,
            need_shipping_address=True,
            is_flexible=False
        )
        
async def pre_checkout_query(pre_checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)
    
async def successful_payment(message: Message):
    wsg = f"Thank you for your order {message.successful_payment.total_amount // 100}"
    await bot.send_message(message.chat.id, wsg)
    
def rregister_handler_pay(dispatcher_: Dispatcher):
    dispatcher_.register_message_handler(start, commands=['Buy'])