def is_acceptable_password(password: str) -> bool:
    return bool(password[6:])
# return len(password) > 6


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
