import aiogram.fsm.state as state

class JoinState(state.StatesGroup):
    code = state.State()
