def is_majority(items: list[bool]) -> bool:
    true = 0
    false = 0
    for (offset, item) in enumerate(items):
        print("Item:", item, "Offset:", offset)
        if item is True:
            true += 1
        elif item is False:
            false += 1
    if true > false:
        return True
    else:
        return False


# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
