dgits = {"1","2","3","4","5","6","7","8","9"}

def is_acceptable_password(password: str) -> bool:

    if bool(password[6:]):
        password = set(password)
        if len(dgits & password) != 0 and len(password-dgits) != 0:
            return True
    return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False