

def check_user_id(callback_user_id: int, user_id: dict) -> bool:
    if callback_user_id == user_id:
        return True
    else:
        return False
