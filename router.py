import logging
from pathlib import Path

from aiogram import F, Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, User, ContentType, File

import texts
import config
from filters import EndWordFilter
from parse_anec import parse_anec

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

# @router.message(Command('speech'))
# async def forawardHandler(message: Message):
#     try:
#         am: Message = await message.reply_to_message
#         if am.content_type == "voice":
#             downloaded_file =  
#         # downloaded_file = bot.download_file(file_info.file_path)
 
#         # Convert the voice message to text
#         r = sr.Recognizer()
#         with sr.AudioFile(downloaded_file) as source:
#             audio_data = r.record(source)
#             text = r.recognize_google(audio_data, language='ru-RU')
 
#         # Send the text message back to the user
#         bot.reply_to(message, text)
#     except Exception as e:
#         # Log the error
#         print(f"Error: {e}")
#         bot.reply_to(message, "Sorry, I couldn't convert your voice message to text. Please try again later.")

# @router.message(Command('reply'))
# async def replyHandler(message: Message):
    # await message.reply_to_message.forward(-4005445963)
    # await message.answer(message.reply_to_message.content_type)

@router.message(EndWordFilter())
async def daHandler(message: Message):
    def getAnswer():
        if message.text in v_keys:
            return texts.REPLIES.get(message.text)
        else:
            return texts.REPLIES.get(message.text.lower())
    
    await message.answer(getAnswer())

# @router.message(F.text)
# async def twoHandler(message: Message):
    # if len(message.text) > 4:
        # await message.answer("хуе" + message.text[2:])