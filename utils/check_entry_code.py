
def check_entry_code(test: dict, entry_code: str) -> bool:
    
    if test["entry_code"] == entry_code:
        return True
    else:
        return False
