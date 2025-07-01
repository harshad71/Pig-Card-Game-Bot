from aiogram import Router




from ..middleware.admin_middleware import AdminMiddleware



admin_router = Router()
admin_router.message.middleware(AdminMiddleware())

