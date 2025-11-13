import aiogram.fsm.state as state

class Join_state(state.StatesGroup):
    code = state.State()