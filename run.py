# Aiogram imports
from aiogram import Dispatcher, Bot
from app.handlers import main_router
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from aiogram.client.default import DefaultBotProperties

# Other imports
import asyncio, os
from dotenv import load_dotenv


load_dotenv()
bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode="html"))
dp = Dispatcher()
i18n = I18n(path='app/locales', domain='messages')
i18n_handler = SimpleI18nMiddleware(i18n)
i18n_handler.setup(dp)

async def main():
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
