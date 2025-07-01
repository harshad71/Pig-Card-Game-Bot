from aiogram import Router

from .game_handlers import game_router
from .admin_handlers import admin_router

from ..middleware.sub_middleware import SubscriptionMiddleware


main_router = Router()
main_router.include_routers(game_router, admin_router)