from aiogram import Bot
from aiogram.types import Message
from aiogram.enums.chat_member_status import ChatMemberStatus

from .games.pig import PigConfig

import random


async def user_not_left(target_channel_username: int, event: Message, bot: Bot) -> bool:
    member = await bot.get_chat_member(target_channel_username, event.from_user.id)
    if member.status != ChatMemberStatus.LEFT:
        return True
    return False

async def serialize_users_amount(users_amount: str) -> bool:
    if users_amount.isdigit() and int(users_amount) in range(PigConfig.min_users, PigConfig.max_users + 1):
        return True
    return False

async def first_step(users_amount: int) -> int:
    random_user = random.randint(1, users_amount)
    ...

# async def language_id_is_valid(language_id: str) -> bool:
#     if language_id.isdigit() and int(language_id) in LANGUAGE_CODES.keys():
#         return True
#     return False


