import re

def is_acceptable_password(password: str) -> bool:
    wzorzec = re.compile(r'password')
    wynik = wzorzec.findall(password.lower())
    if len(wynik) != 0:
        return False
    if len(password) > 9:
        return True
    if len(password) > 6 and len(password) < 9:
        output1, output2 = re.findall(r'[0-9]',password),re.findall(r'[A-Za-z]',password)
        if len(output1) and len(output2) > 1:
            return True
        else:
            return False
    return False

assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
