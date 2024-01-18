from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message

from texts import REPLIES

class EndWordFilter(BaseFilter):
    # def __init__(self, word: str) -> None:
        # self._word = word                

    async def __call__(self, message: Message) -> bool:
        res = False

        words = message.text.split()

        if words[-1] in REPLIES.values().mapping:
            res = True
        elif words[-1].lower() in REPLIES.values().mapping:
            res = True

        return res