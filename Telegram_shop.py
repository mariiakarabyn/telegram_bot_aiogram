from aiogram import executor
from create_imports import dispatcher_
from handlers import client, admin, pay
from database import SQL_db

client.register_handler_client (dispatcher_)
admin.register_handler_admin (dispatcher_)
pay.rregister_handler_pay (dispatcher_)

async def on_startup(_):
    print('Bot is online')
    SQL_db.sql_start()
    
if __name__ == "__main__":
    executor.start_polling(dispatcher_, skip_updates=True, on_startup=on_startup)
