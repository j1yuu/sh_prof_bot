import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import texts
from filters import EndWordFilter

logger = logging.getLogger('aiogram.dispatcher')
router = Router()
v_keys = texts.REPLIES.values().mapping

# Команды

@router.message(Command('info'))
async def helpHandler(message: Message):
    await message.answer(texts.INFO_TEXT)

@router.message(Command('start'))
async def startHandler(message: Message):
    await message.answer(texts.START_TEXT)
    await message.answer(texts.START_TEXT_SECOND)

@router.message(Command('anecdote'))
async def anecdoteHandler(message: Message):
    # await message.answer(parse_anec()) 
    await message.answer("Пока что не выучил, но скоро будут!")

@router.message(EndWordFilter())
async def daHandler(message: Message):
    def getAnswer():
        if message.text in v_keys:
            return texts.REPLIES.get(message.text)
        else:
            return texts.REPLIES.get(message.text.lower())
    
    await message.answer(getAnswer())