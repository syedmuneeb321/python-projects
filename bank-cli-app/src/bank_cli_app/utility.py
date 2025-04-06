import random

def generate_pin() -> str:
    pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return pin

def generate_account_number() -> str:
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    account_number = ''.join(random.choice(characters) for _ in range(10))  
    return account_number
print("")