from aiogram.fsm.state import StatesGroup, State


class GameOnline(StatesGroup):
    users_amount = State()
    donation_sum = State()

class GameWithRobot(StatesGroup):
    users_amount = State()