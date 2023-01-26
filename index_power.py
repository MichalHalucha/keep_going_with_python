def index_power(array: list[int], n: int) -> int:
    try:
        return array[n]**n
    except:
        return -1


# These "asserts" are used for self-checking
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")
