import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import tokens
from router import router
import logger_init

bot = Bot(token=tokens.BOT_TOKEN, parse_mode=ParseMode.HTML)

async def main():
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    bot_task = asyncio.create_task(dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types()))

    await bot_task

if __name__ == '__main__':
    logger_init.loggerInit()
    logger = logging.getLogger('aiogram.dispatcher')
    asyncio.run(main())