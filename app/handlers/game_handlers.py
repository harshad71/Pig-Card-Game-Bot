from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from aiogram.utils.i18n import gettext as _


from ..utils import serialize_users_amount
from ..text.ru import BaseText, GameText
from ..data import INSTAGRAM_LINKS, EMAIL_LINKS, DEVELOPER
from ..keyboards.univ import main_menu_keyboard, build_game_kb, \
                             github_source_code_link_kb, game_modes_keyboard, \
                             build_users_amount_kb

from ..fsm import GameOnline, GameWithRobot
from ..middleware.sub_middleware import SubscriptionMiddleware

from ..games.pig import Pig



game_router = Router()
game_router.message.middleware(SubscriptionMiddleware())


@game_router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    botname = await bot.get_my_name()
    await message.answer(text=_(await BaseText.start_message(message.from_user.username, botname=botname.name)), reply_markup=main_menu_keyboard)

@game_router.message(F.text == 'Об игре ❓')
@game_router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(text=_(GameText.pig), reply_markup=await build_game_kb())

@game_router.message(F.text == '[ Project source code ]')
@game_router.message(Command('project_source_code'))
async def cmd_about(message: Message):
    await message.answer(text=_(await BaseText.project_info(DEVELOPER, INSTAGRAM_LINKS, EMAIL_LINKS)), reply_markup=github_source_code_link_kb)

@game_router.message(F.text == 'Играть ▶️')
@game_router.callback_query(F.data == 'play_pig')
@game_router.message(Command('play'))
async def cmd_play(message: Message):
    await message.answer(text=_(GameText.select_game_mode), reply_markup=game_modes_keyboard)


# GAME WITH A ROBOT
# ------------------------------------------------------------------------------------------
@game_router.callback_query(F.data == 'play_with_robot')
async def cmd_play_with_robot_1(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=_(GameText.select_users_amount), reply_markup=await build_users_amount_kb())
    await state.set_state(GameWithRobot.users_amount)

@game_router.callback_query(GameWithRobot.users_amount)
async def cmd_play_with_robot_2(callback: CallbackQuery):
    users_amount = callback.data[5:]
    if await serialize_users_amount(users_amount):
        pig_game = await Pig.create(users_amount)


# ------------------------------------------------------------------------------------------

# GAME WITH USERS
# ------------------------------------------------------------------------------------------
@game_router.callback_query(F.data == 'play_with_users')
async def cmd_play_with_users_1(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=_(GameText.select_users_amount), reply_markup=await build_users_amount_kb())
    await state.set_state(GameOnline.users_amount)

@game_router.callback_query(GameOnline.users_amount)
async def cmd_play_with_users_2(callback: CallbackQuery, state: FSMContext):
    users_amount = callback.data[5:]
    if await serialize_users_amount(users_amount):
        await callback.message.answer(text=_(GameText.input_donation_sum))
        await state.set_state(GameOnline.donation_sum)


@game_router.callback_query(GameOnline.donation_sum)
async def cmd_play_with_users_2(callback: CallbackQuery, state: FSMContext):
    ...