def is_even(num: int) -> bool:
    x = int.__divmod__(num, 2)
    return bool(x[1] == 0)

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True