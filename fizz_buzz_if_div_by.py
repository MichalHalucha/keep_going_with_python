def checkio(number: int) -> str:
    x = int.__divmod__(number, 3)
    y = int.__divmod__(number, 5)
    if bool(x[1] == 0) & bool(y[1] == 0):
        return "Fizz Buzz"
    if bool(x[1] == 0):
        return "Fizz"
    elif bool(y[1] == 0):
        return "Buzz"
    else:
        return str(number)


assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"