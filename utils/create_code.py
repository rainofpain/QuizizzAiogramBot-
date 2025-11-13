import random 

def create_code() -> str:
    code = ""
    
    for number in range(6):
        code += str(random.randint(0,9))
    
    return code    
