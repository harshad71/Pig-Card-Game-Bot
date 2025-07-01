from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from aiogram.utils.i18n import gettext as _

from ..text.ru import BaseText
from ..utils import user_not_left
from ..data import CHANNELS_USERNAMES
from ..keyboards.univ import channels_to_subscribe_kb 

from typing import Callable, Awaitable, Dict, Any


class SubscriptionMiddleware(BaseMiddleware):
    '''Middleware to check if a user is subscribed on all required channels.'''

    async def __call__(self, 
                handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
                event: Message | CallbackQuery,
                data: Dict[str, Any]) -> Any:

        if all([await user_not_left(username, event, event.bot) for username in CHANNELS_USERNAMES.keys()]):
            return await handler(event, data)
        else:
            await event.message.answer(text=_(BaseText.not_subscribed_error), reply_markup=await channels_to_subscribe_kb)