from aiogram.fsm.state import State, StatesGroup



class ClientForm(StatesGroup):
    name = State()