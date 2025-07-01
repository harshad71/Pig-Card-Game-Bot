from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from aiogram.utils.i18n import gettext as _

from ..text.ru import BaseText

import os
from dotenv import load_dotenv
from typing import Callable, Awaitable, Dict, Any


class AdminMiddleware(BaseMiddleware):
    '''Middleware to check if a user is staff (admin).'''

    async def __call__(self, 
                handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
                event: Message | CallbackQuery,
                data: Dict[str, Any]) -> Any:
        
        load_dotenv()
    
        if event.from_user.id in [int(uid) for uid in os.getenv('STAFF').split(',')]:
            return await handler(event, data)
        else:
            await event.message.answer(text=_(BaseText.command_not_found))
