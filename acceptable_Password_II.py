dgits = {"1","2","3","4","5","6","7","8","9"}

def is_acceptable_password(password: str) -> bool:
    if bool(password[6:]):
        password = set(password)
        if len(dgits & password) != 0:
            return True
    return False
# return len(password) > 6 and any(ch.isdigit() for ch in password)
# is_acceptable_password = lambda p: len(p)>6 and any([l.isdigit() for l in p])

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
