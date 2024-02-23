from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
import os

storage_ = MemoryStorage()

load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN'))
dispatcher_ = Dispatcher(bot, storage=storage_)