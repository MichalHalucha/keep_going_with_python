def checkio(array: list[int]) -> int:
    index = 0
    value = 0
    if len(array) == 1:
        return array[0]*array[0]
    elif len(array) > 1:
        try:
            for i in range(len(array)):
                value = value + array[index]
                index += 2
                print(value)
        except:
            return value * array[-1]
    return 0


assert checkio([6]) == 36
assert checkio([]) == 0
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30



print("The mission is done! Click 'Check Solution' to earn rewards!")
