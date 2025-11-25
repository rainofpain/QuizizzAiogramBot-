import aiogram.fsm.state as state

class LobbyAuthorizationState(state.StatesGroup):
    lobby_name = state.State()
