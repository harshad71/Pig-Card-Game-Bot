from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..games.pig import PigConfig
from ..data import GAMES_CALLBACK_LINKS, CHANNELS_USERNAMES, GITHUB_SOURCE_CODE_LINK


main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Играть ▶️'), KeyboardButton(text='Об игре ❓')],
    [KeyboardButton(text='[ Project source code ]')]], 
    resize_keyboard=True)

flip_card_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перевернуть карту...', callback_data='flip_card')]])

github_source_code_link_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Check out code on Github', url=GITHUB_SOURCE_CODE_LINK)]])

game_modes_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть с роботом', callback_data='play_with_robot')],
    [InlineKeyboardButton(text='Играть онлайн', callback_data='play_with_users')]])

async def channels_to_subscribe_kb() -> InlineKeyboardMarkup:
    ''' '''
    keyboard = InlineKeyboardBuilder()
    for value  in CHANNELS_USERNAMES.values():
        keyboard.add(InlineKeyboardButton(text=value[0], url=value[1]))
    keyboard.adjust(1)
    return keyboard.as_markup()

async def build_users_amount_kb() -> InlineKeyboardMarkup:
    ''' '''
    keyboard = InlineKeyboardBuilder()
    for amount in range(PigConfig.min_users, PigConfig.max_users + 1):
        keyboard.add(InlineKeyboardButton(text=str(amount), callback_data=f'play_{amount}'))
    keyboard.adjust()
    return keyboard.as_markup()


async def build_game_kb() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Играть', callback_data='play_pig'))
    keyboard.add(InlineKeyboardButton(text='Правила', callback_data='rules_pig'))
    keyboard.add(InlineKeyboardButton(text='Подробнее', url=GAMES_CALLBACK_LINKS['pig']))
    keyboard.adjust(2, 1)
    return keyboard.as_markup()

