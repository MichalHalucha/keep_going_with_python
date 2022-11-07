def number_length(value: int) -> int:
    return len(str(value))


assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2