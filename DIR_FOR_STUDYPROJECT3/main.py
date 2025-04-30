from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
import asyncio
import logging
from core.settings import settings
from aiogram.enums import ParseMode #для форматирования стилей
from aiogram.client.bot import DefaultBotProperties #для форматирования стилей
token = 'TOKEN=7795110762:AAHSsDeG1VE9hwlcVo7A0lzKH-5GMHdeO_k'


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())