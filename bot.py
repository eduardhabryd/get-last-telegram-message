import asyncio
import logging
import sys
from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from send import send_rabbit

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

messages = []


@dp.message(Command("print"))
async def command_start_handler(message: Message) -> dict:
    last_message = messages[-1]
    await message.answer(f"Last message was printed: {last_message}")
    send_rabbit(f"print {last_message}")


@dp.message(Command("send"))
async def command_start_handler(message: Message) -> dict:
    last_message = messages[-1]
    await message.answer(f"Last message was send: {last_message}")
    send_rabbit(f"send {last_message}")


@dp.message()
async def message_loger(message: types.Message) -> None:
    messages.append(message.text)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
