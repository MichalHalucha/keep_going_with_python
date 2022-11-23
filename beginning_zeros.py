def beginning_zeros(a: str) -> int:
    zeros = list(a)
    numbers_of_zeros = []
    for i in zeros:
        print(i)
        if i == '0':
            print("siema")
            numbers_of_zeros.append(i)
            print(numbers_of_zeros)
        else:
            return len(numbers_of_zeros)
    return len(zeros)


assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
