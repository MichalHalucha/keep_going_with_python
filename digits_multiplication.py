def checkio(number: int) -> int:
    number = list(str(number))
    sum=1
    for i in number:
        if int(i) != 0:
            sum = sum * int(i)
    return sum

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
