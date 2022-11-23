import re
def is_all_upper(text: str) -> bool:
    if len(list(text.rstrip(" ")))==0: return True
    output2 = re.findall(r'[0-9]', text)
    print(len(output2))
    if len(output2) > 0:
        return True
    for i in text.split(" "):
        if i.isupper():
            return True
        else:
            return False

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True
assert is_all_upper('     ') == True


print("The mission is done! Click 'Check Solution' to earn rewards!")
