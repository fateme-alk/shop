import re

def validate_phone(number: str) -> bool:
    pattern1 = '^[0][9]\d{9}$'
    pattern2 = '^[\+][9][8]\d{10}$'
    pattern3 = '^[0][0][9][8][9]\d{9}$'
    if re.match(pattern1, number):
        return True
    elif re.match(pattern2, number):
        return True
    elif re.match(pattern3, number):
        return True
    else:
        return False

def validate_email(email: str) -> bool:
    pattern = '^[a-zA-Z0-9_\.]+@([a-zA-Z|0-9])+\.[a-zA-Z]{3}$'
    if re.match(pattern, email):
        return True
    else:
        return False